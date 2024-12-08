class Position:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
    def __repr__(self):
        return str(self.x) + "," + str(self.y) + ", direction: " + self.d
    def __str__(self):
        return str(self.x) + "," + str(self.y) + ", direction: " + self.d

map = []
start = Position(0, 0, "n")

with open("data/day6", "r") as f:
    for i, line in enumerate(f):
        temp = line.find("^")
        if temp > 0:
            start.x = temp
            start.y = i
            start.d = "n"
        map.append(list(line.strip()))

height = len(map)
width  = len(map[0])

def newmap():
    return [["." for _ in range(width)] for _ in range(height)]

def step(p, tempmap):
    if (p.y == height-1 and p.d == "s") or\
       (p.x == width -1 and p.d == "e") or\
       (p.y == 0        and p.d == "n") or\
       (p.x == 0        and p.d == "w"):
        return Position(-1, -1, "x")
    match(p.d):
        case "n":
            if tempmap[p.y-1][p.x] in "#":
                p.d = "e"
            else:
                p.y -= 1
                tempmap[p.y][p.x] = "x"
        case "e":
            if tempmap[p.y][p.x+1] in "#":
                p.d = "s"
            else:
                p.x += 1
                tempmap[p.y][p.x] = "x"
        case "s":
            if tempmap[p.y+1][p.x] in "#":
                p.d = "w"
            else:
                p.y += 1
                tempmap[p.y][p.x] = "x"
        case "w":
            if tempmap[p.y][p.x-1] in "#":
                p.d = "n"
            else:
                p.x -= 1
                tempmap[p.y][p.x] = "x"
    return p

refmap = newmap()
expmap = newmap()

for i in range(height):
    for j in range(width):
        refmap[i][j] = map[i][j]

# refmap is kept clean as initial file
# map will be part 1 answer
# expmap is cache for part 2

current = Position(start.x, start.y, start.d)
while(0 < current.x < width and 0 < current.y < height):
    current = step(current, map)

count = 0
for l in map:
    for p in l:
        if p == "x":
            count += 1

print("\n".join("".join(l) for l in map))
print(count)

countp2 = 0
progress = 0

for i in range(height):
    for j in range(width):
        # only try places on path of part 1
        if map[i][j] == "x":
            progress += 1

            # set up new expmap
            for ii in range(height):
                for jj in range(width):
                    expmap[ii][jj] = refmap[ii][jj]
            expmap[i][j] = "#"

            # try out this new map
            current = Position(start.x, start.y, start.d)
            temploc = Position(current.x, current.y, current.d)
            history = [temploc]

            while(0 < current.x < width and 0 < current.y < height):
                current = step(current, expmap)
                # check if we have been here before
                found = False
                for pos in history:
                    if current.x == pos.x and current.y == pos.y and current.d == pos.d:
                        found = True
                if found:
                    print("found one! ", i, " ", j)
                    countp2 += 1
                    break
                # check if there's a direction change and record in history
                elif current.d != history[-1].d:
                    temploc = Position(current.x, current.y, current.d)
                    history.append(temploc)

            print(progress, "/", count)
            # reset expmap to refmap
            for ii in range(height):
                for jj in range(width):
                    expmap[ii][jj] = refmap[ii][jj]

print(countp2)

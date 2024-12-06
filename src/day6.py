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
current = Position(0, 0, "n")

with open("data/day6", "r") as f:
    for i, line in enumerate(f):
        temp = line.find("^")
        if temp > 0:
            current.x = temp
            current.y = i
            current.d = "n"
        map.append(list(line.strip()))

height = len(map)
width  = len(map[0])

mapp2 = [["." for _ in range(width)] for _ in range(height)]
print(mapp2)
for i in range(height):
    for j in range(width):
        mapp2[i][j] = map[i][j]

def step(p):
    if (p.y == height-1 and p.d == "s") or\
       (p.x == width -1 and p.d == "e") or\
       (p.y == 0        and p.d == "n") or\
       (p.x == 0        and p.d == "w"):
        return Position(-1, -1, "x")
    match(p.d):
        case "n":
            if map[p.y-1][p.x] in "#":
                p.d = "e"
            else:
                p.y -= 1
                map[p.y][p.x] = "x"
        case "e":
            if map[p.y][p.x+1] in "#":
                p.d = "s"
            else:
                p.x += 1
                map[p.y][p.x] = "x"
        case "s":
            if map[p.y+1][p.x] in "#":
                p.d = "w"
            else:
                p.y += 1
                map[p.y][p.x] = "x"
        case "w":
            if map[p.y][p.x-1] in "#":
                p.d = "n"
            else:
                p.x -= 1
                map[p.y][p.x] = "x"
    return p

while(0 < current.x < width and 0 < current.y < height):
    current = step(current)

count = 0
for l in map:
    for p in l:
        if p == "x":
            count += 1

print("\n".join("".join(l) for l in map))
print(count)


print("\n".join("".join(l) for l in mapp2))
maps = []
for i in range(height):
    for j in range(width):
        pass


temploc = Position(current.x, current.y, current.d)
history = [temploc]

while(0 < current.x < width and 0 < current.y < height):
    if current.d != history[-1].d:
        temploc = Position(current.x, current.y, current.d)
        history.append(temploc)
    current = step(current)


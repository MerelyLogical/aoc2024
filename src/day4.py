a = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

data = []
with open("data/day4", "r") as f:
    for line in f:
        data.append(line.strip())

count = 0
height = len(data)
width  = len(data[0])
print (data, height, width)
for i in range(height):
    for j in range(width):
        if data[i][j] == "X":
            # down
            if i < height - 3:
                if data[i+1][j] + data[i+2][j] + data[i+3][j] == "MAS":
                    count += 1
                    print (i, j, "d")
            # right 
            if j < width - 3:
                if data[i][j+1] + data[i][j+2] + data[i][j+3] == "MAS":
                    count += 1
                    print (i, j, "r")
            # up
            if i > 2:
                if data[i-1][j] + data[i-2][j] + data[i-3][j] == "MAS":
                    count += 1
                    print (i, j, "u")
            # left
            if j > 2:
                if data[i][j-1] + data[i][j-2] + data[i][j-3] == "MAS":
                    count += 1
                    print (i, j, "l")

            # upleft
            if i > 2 and j > 2:
                if data[i-1][j-1] + data[i-2][j-2] + data[i-3][j-3] == "MAS":
                    count += 1
                    print (i, j, "ul")
            # upright
            if i > 2 and j < width - 3:
                if data[i-1][j+1] + data[i-2][j+2] + data[i-3][j+3] == "MAS":
                    count += 1
                    print (i, j, "ur")
            # downleft
            if i < height - 3 and j > 2:
                if data[i+1][j-1] + data[i+2][j-2] + data[i+3][j-3] == "MAS":
                    count += 1
                    print (i, j, "dl")
            # downright
            if i < height - 3 and j < width - 3:
                if data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3] == "MAS":
                    count += 1
                    print (i, j, "dr")

print(count)

count = 0
for i in range(height):
    for j in range(width):
        if data[i][j] == "A":
            if i < height - 1 and j < width - 1 and i > 0 and j > 0:
                if ((data[i-1][j-1] == "M" and data[i+1][j+1] == "S") or \
                    (data[i-1][j-1] == "S" and data[i+1][j+1] == "M")) and \
                   ((data[i-1][j+1] == "M" and data[i+1][j-1] == "S") or \
                    (data[i-1][j+1] == "S" and data[i+1][j-1] == "M")):
                    count += 1

print(count)

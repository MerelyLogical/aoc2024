import re

with open("data/day3", 'r') as f:
    sum = 0
    for line in f:
        mullist = re.findall("mul\((\d{,3}),(\d{,3})\)", line)
        for mulpair in mullist:
            sum += int(mulpair[0]) * int(mulpair[1])

print(sum)

data = ""
with open("data/day3", 'r') as f:
    for line in f:
        data += line

sum = 0
splitlines = data.split("do()")
for new_line in splitlines:
    doline = new_line.split("don't()")[0]
    mullist = re.findall("mul\((\d{,3}),(\d{,3})\)", doline)
    for mulpair in mullist:
        sum += int(mulpair[0]) * int(mulpair[1])

print(sum)

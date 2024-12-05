rules = {}
parsing_rules = True
data = []

with open("data/day5", "r") as f:
    for line in f:
        if line == "\n":
            break
        temp = line.strip().split("|")
        if temp[0] in rules:
            rules[temp[0]].add(temp[1])
        else:
            rules[temp[0]] = {temp[1]}
    
    print(rules)

    count = 0
    for line in f:
        if line == "\n":
            continue
        else:
            pages = line.strip().split(",")
            data.append(pages)
            ordered = True
            for i in range(1, len(pages)):
                if pages[i] in rules:
                    # not correctly ordered
                    if rules[pages[i]].intersection(pages[:i]):
                        print(pages, i, rules[pages[i]])
                        ordered = False
                        break

            if ordered:
                count += int(pages[len(pages)//2])

print(count)


count = 0
for line in data:
    ordered = True
    for i in range(1, len(line)):
        for j in range(i):
            if line[i] in rules:
                if line[j] in rules[line[i]]:
                    line[i], line[j] = line[j], line[i]
                    ordered = False
    if not ordered:
        count += int(line[len(line)//2])
        print(line)


print(count)


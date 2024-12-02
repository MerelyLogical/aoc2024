def mat_read(infile):
    temp_mat = []
    with open(infile, 'r') as f:
        for line in f:
            temp_mat.append(list(map(lambda x: int(x), line.split())))
    return temp_mat

def safety_check(line):
    increasing = False
    if line[1] > line[0]:
        increasing = True
    elif line[1] == line[0]:
        return False
    prev_num = line[0]

    for num in line[1:]:
        if increasing:
            if not 0 < num - prev_num < 4:
                return False
        else:
            if not 0 < prev_num - num < 4:
                return False
        prev_num = num
    return True

def dampener(line):
    temp_mat = []
    for i in range(len(line)):
        temp_line = []
        for j in range(len(line)):
            if i != j:
                temp_line.append(line[j])
        temp_mat.append(temp_line)
    return temp_mat

mat = mat_read("data/day2")
safe = 0
for line in mat:
    if safety_check(line):
        safe += 1

print(safe)

safe = 0
for line in mat:
    if safety_check(line):
        safe += 1
    else:
        new_mat = dampener(line)
        for new_line in new_mat:
            unsafe = True
            if safety_check(new_line):
                unsafe = False
                break
        if not unsafe:
            safe += 1

print(safe)
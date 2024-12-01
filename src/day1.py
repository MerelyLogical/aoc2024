data = "data/day1"

left  = []
right = []
with open(data, 'r') as f:
    for line in f:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
        
left.sort()
right.sort()

assert(len(left) == len(right)) 

dist = 0
for i in range(len(left)):
    dist += abs(left[i] - right[i])

print("distance is: " + str(dist))

sim_right = {}
for id in right:
    if id in sim_right:
        sim_right[id] += id
    else:
        sim_right[id] = id

sim = 0
for id in left:
    if id in sim_right:
        sim += sim_right[id]

print("similiarity score is: " + str(sim))

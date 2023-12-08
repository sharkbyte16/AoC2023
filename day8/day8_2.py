import math

print("\033c", end='')  # clear terminal

f = open('day8/day8_2_test.txt', 'r')
f = open('day8/day8_1.txt', 'r')
input = [ line.strip() for line in f.readlines()]
directions = list(map(int, list(input[0].replace('L', '0').replace('R','1'))))
nodes = {}
for s in input[2::]:    
    key = s.split(' = ')[0]
    L = s.split(' = ')[1].replace('(', '').replace(')', '').split(', ')[0]
    R = s.split(' = ')[1].replace('(', '').replace(')', '').split(', ')[1]
    nodes[key] = (L, R)
keys = nodes.keys()

start = [key for key in keys if key[2]=='A']
end = [key for key in keys if key[2]=='Z']

next = []
i = 0
while True:
    for node in start:
        next.append(nodes[node][directions[i % len(directions)]])
    i += 1    
    sum = 0     # count non-Z-ending, if 0 than all are z-ending
    for node in next:
        if node[2] != 'Z':
            sum += 1
    if sum < 1:
        break
    start = next.copy()
    next = []
print(i)


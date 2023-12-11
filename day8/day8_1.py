import math

print("\033c", end='')  # clear terminal

f = open('day8/day8_1_test2.txt', 'r')
f = open('day8/day8_1.txt', 'r')
input = [ line.strip() for line in f.readlines()]
directions = list(map(int, list(input[0].replace('L', '0').replace('R','1'))))
nodes = {}
for s in input[2::]:    
    key = s.split(' = ')[0]
    L = s.split(' = ')[1].replace('(', '').replace(')', '').split(', ')[0]
    R = s.split(' = ')[1].replace('(', '').replace(')', '').split(', ')[1]
    nodes[key] = (L, R)

next = 'AAA'
i = 0
while True:
    next = nodes[next][directions[i % len(directions)]]
    i += 1    
    if next == 'ZZZ':
        break
print('steps', i)
    


from math import gcd

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
#['QXA', 'PDA', 'TDA', 'QQA', 'PPA', 'AAA']

cycles = []
for node in start:
    i = 0
    while True:
        next = nodes[node][directions[i % len(directions)]]
        i += 1            
        if next[2] == 'Z':
            break
        node = next
        next = ''
    cycles.append(i)

print(cycles)

# now find least common multiple in the cycles of the starting points
lcm = cycles.pop()
for num in cycles:
    lcm = lcm*num // gcd(lcm, num)

print(lcm)
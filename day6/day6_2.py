import math

print("\033c", end='')  # clear terminal

f = open('day6/day6_1_test.txt', 'r')
f = open('day6/day6_1.txt', 'r')
input = [ list(map(int, [line.strip().split(':')[1::][0].replace(' ', '')])) for line in f.readlines()]
print(input)

def quadratic_real_roots(a, b, c):
    D = b**2 - 4*a*c
    if D >= 0:
        roots = [ (-b + math.sqrt(D))/(2*a), (-b - math.sqrt(D))/(2*a) ] 
        roots.sort()
        return roots
    else:
        return ('im', 'im')

product = 1
for i in range(len(input[0])):
    t_race = input[0][i]
    distance = input[1][i]
    t_press = quadratic_real_roots(1, -t_race, distance)
    ways = math.ceil(t_press[1])-math.floor(t_press[0]+1)
    print(t_press, math.floor(t_press[0]+1), math.ceil(t_press[1]), ways)
    product *= ways

print(product)

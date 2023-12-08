print("\033c", end='')
input = ['467..114..',
         '...*......',
         '..35...633',
         '.......#..',
         '617*......',
         '.....+.58.',
         '..592.....',
         '......755.',
         '...$.*....',
         '.664.598..']
f = open('day3/day3_1.txt', 'r')
input = [line.strip() for line in f.readlines()]

#input = input[0:10]

numbers_found = []    # list of found numbers in format [nr, y, start_x, len]
for y in range(len(input)):
    nr = ''
    for x in range(len(input[y])):        
        c = input[y][x]
        if c.isdigit():
            nr += c                        
        else:
            if nr != '':
                numbers_found.append([int(nr), y, x-len(nr), len(nr)])
                nr = ''
    if nr != '':
        numbers_found.append([int(nr), y, x-len(nr)+1, len(nr)])
    nr = ''

def partnumber(input, ymax, xmax, number):
    adjacent_symbol = False
    y_start = max(number[1]-1,0)
    y_end = min(number[1]+1, ymax)+1
    x_start = max(number[2]-1,0)
    x_end = min(number[2]+number[3], xmax)+1
    for y in range(y_start, y_end):
        for x in range(x_start, x_end):
            c = input[y][x]
            #print(c)
            if (not c.isnumeric()) & (c != '.'):
                adjacent_symbol = True
    return adjacent_symbol

sum = 0
for n in numbers_found:
    #print(n[0])
    if partnumber(input, len(input)-1, len(input[0])-1, n):
        #print(n[0])
        sum += n[0]
print(sum)



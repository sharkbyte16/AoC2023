import numpy as np

print("\033c", end='')
input = ['467..114..',
         '...*......',
         '..35..633.',
         '......#...',
         '617*......',
         '.....+.58.',
         '..592.....',
         '......755.',
         '...$.*....',
         '.664.598..']
f = open('day3/day3_1.txt', 'r')
input = [line.strip() for line in f.readlines()]

ymax = len(input)-1
xmax = len(input[0])-1

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
            if (not c.isnumeric()) & (c != '.'):
                adjacent_symbol = True
    return adjacent_symbol

partnumbers_found = []
for nr in numbers_found:
    y = nr[1]
    xstart = nr[2]
    xend = xstart + nr[3]    
    if partnumber(input, ymax, xmax, nr):
        partnumbers_found.append(nr)

#############

npinput = np.zeros((ymax+1, xmax+1), np.int64)
partnr_dict = {}
for i in range(len(partnumbers_found)):
    y = partnumbers_found[i][1]
    xstart = partnumbers_found[i][2]
    xend = xstart + partnumbers_found[i][3]
    for x in range(xstart, xend):        
        assert input[y][x].isdigit
        npinput[y][x] = i+1   #
        partnr_dict[i+1] = partnumbers_found[i][0]

ratios_found = []
count = 0
for y in range(len(input)):    
    for x in range(len(input[y])):        
        c = input[y][x]
        if c == '*':        
            adjacent_parts = []            
            for yc in range(max(y-1, 0), min(y+1, ymax)+1):
                for xc in range(max(x-1, 0), min(x+1, xmax)+1):
                    if npinput[yc][xc] != 0:
                        adjacent_parts.append(npinput[yc][xc])
            adjacent_parts_set = set(adjacent_parts)            
            adjacent_parts = list(adjacent_parts_set)            
            if len(adjacent_parts_set) == 2:
                ratios_found.append(partnr_dict[adjacent_parts[0]]*partnr_dict[adjacent_parts[1]])
                count += 1
                print('gear', count, 'row,col:', y+1, x+1, '-->', partnr_dict[adjacent_parts[0]], '*',partnr_dict[adjacent_parts[1]], '=', partnr_dict[adjacent_parts[0]]*partnr_dict[adjacent_parts[1]])

print(sum(ratios_found))

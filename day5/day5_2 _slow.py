import sys
import time

print("\033c", end='')  # clear terminal

f = open('day5/day5_1_test.txt', 'r')
f = open('day5/day5_1.txt', 'r')
input = [line.strip().replace(':', '').replace('-','_').split() for line in f.readlines() if line.strip() != '']


seeds = []
maps = {}
section = ''
for line in input:    
    if not line[0][0].isdigit():    
        section = line[0]
        if section == 'seeds':
            line.pop(0)                     # remove first element, here 'seeds'
            seeds = list(map(int, line))    # assign after conversion to integer list
            assert len(seeds) % 2 == 0
    else:
        line = list(map(int, line))         # convert string list to integer list
        if section not in maps.keys():
            maps[section] = []              # add section list if not existing
        maps[section].append([range(line[1], line[1]+line[2]), line[0]-line[1]])    # range and delta

def convert(section_data, nr_in):
    nr_out = []
    for mapping in section_data:
        if nr_in in mapping[0]:
            nr_out.append(nr_in + mapping[1])
    assert len(nr_out) < 2
    if len(nr_out) == 0:
        return nr_in
    else:
        return nr_out[0]

to_do = 0
for i in range(0, len(seeds), 2):
    to_do += seeds[i+1]
print(to_do)

ts = time.time()
lowest_location = sys.maxsize
done = 0
for i in range(0, len(seeds), 2):
    for seed in range(seeds[i], seeds[i]+seeds[i+1]): 
        soil = convert(maps['seed_to_soil'], seed)
        fertilizer = convert(maps['soil_to_fertilizer'], soil)
        water = convert(maps['fertilizer_to_water'], fertilizer)
        light = convert(maps['water_to_light'], water)
        temperature = convert(maps['light_to_temperature'], light)
        humidity = convert(maps['temperature_to_humidity'], temperature)
        location = convert(maps['humidity_to_location'], humidity)        
        if location < lowest_location:
            lowest_location = location
        done += 1
        if done == 1000000:
            print('ETA(s) ', to_do/1000000*(time.time()-ts))
        
print(lowest_location)

# answer: 108956227
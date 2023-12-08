input = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
f = open('day2/day2_1.txt', 'r')
input = f.readlines()

parsed = []
for line in input:    
    gamenr_str = line.split(':')[0]
    gamenr = int(gamenr_str.split(' ')[1])    
    games_played_str = line.split(':')[1].strip()
    games_played = games_played_str.split(';')    
    for i in range(len(games_played)):
        games_played[i] = games_played[i].split(',')
        for j in range(len(games_played[i])):
            games_played[i][j] = games_played[i][j].strip().split(' ')
    parsed.append(games_played)

power_sum = 0
for game in range(len(parsed)):
    minimal_RGB = [0, 0, 0]            
    for draw in parsed[game]:        
        for color in draw:            
            match color[1]:
                case 'red':
                    if int(color[0]) > minimal_RGB[0]:
                        minimal_RGB[0] = int(color[0])
                case 'green':
                    if int(color[0]) > minimal_RGB[1]:
                        minimal_RGB[1] = int(color[0])
                case 'blue':
                    if int(color[0]) > minimal_RGB[2]:
                        minimal_RGB[2] = int(color[0])
    game_power = minimal_RGB[0]*minimal_RGB[1]*minimal_RGB[2]
    power_sum += game_power

print(power_sum)



    


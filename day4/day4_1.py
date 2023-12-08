print("\033c", end='')
"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
f = open('day4/day4_1.txt', 'r')
input = [line.strip() for line in f.readlines()]

total_points = 0
for card in input:
    cardnr = card.split(':')[0].split()[1]
    winning = set(card.split(':')[1].strip().split('|')[0].split())
    draw = set(card.split(':')[1].strip().split('|')[1].split())
    nrinboth = len(draw.intersection(winning))
    points = 2**(nrinboth-1) if nrinboth > 0 else 0
    total_points += points
print(total_points)




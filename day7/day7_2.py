import math

print("\033c", end='')  # clear terminal

cards_dict = {'A':'M', 'K':'L', 'Q':'K', 'T':'J', '9':'I', '8':'H', '7':'G', '6':'F', '5':'E', '4':'D', '3':'C', '2':'B', 'J':'A'}
hand_type_dict = {'Five of a kind':6, 'Four of a kind':5, 'Full house':4, 'Three of a kind':3, 'Two pair':2, 'One pair':1, 'High card':0}

f = open('day7/day7_1_test.txt', 'r')
f = open('day7/day7_1.txt', 'r')
input = [ line.strip().split() for line in f.readlines()]
for hand in input: hand[1] = int(hand[1])

#print(input)

def hand_eval(hand): # returns a tuple with the hand type, type value, card value based on order and its bid
    card_count = {}
    for card in cards_dict.keys(): card_count[card] = 0
    for card in hand[0]: 
        card_count[card] += 1
    five = list(card_count.values()).count(5)
    four = list(card_count.values()).count(4)
    three = list(card_count.values()).count(3)
    two = list(card_count.values()).count(2)
    jokers = card_count['J']       
    value = cards_dict[hand[0][0]] + cards_dict[hand[0][1]] + cards_dict[hand[0][2]] + cards_dict[hand[0][3]] + cards_dict[hand[0][4]]    
    bid = hand[1]
    match jokers:
        case 0: # standard case of part one
            if five == 1:                   return (hand_type_dict['Five of a kind'],  value, bid, hand[0], 'Five of a kind')
            if four == 1:                   return (hand_type_dict['Four of a kind'],  value, bid, hand[0], 'Four of a kind')
            if three == 1 and two == 1:     return (hand_type_dict['Full house'],      value, bid, hand[0], 'Full house')
            if three == 1:                  return (hand_type_dict['Three of a kind'], value, bid, hand[0], 'Three of a kind')
            if two == 2:                    return (hand_type_dict['Two pair'],        value, bid, hand[0], 'Two pair')
            if two == 1:                    return (hand_type_dict['One pair'],        value, bid, hand[0], 'One pair')
            return (hand_type_dict['High card'], value, bid, hand[0], 'High card')
        case 1: # AAAAJ, AAABJ, AABBJ, AABCJ, ABCDJ
            if four == 1:                   return (hand_type_dict['Five of a kind'],  value, bid, hand[0], 'Five of a kind')
            if three == 1:                  return (hand_type_dict['Four of a kind'],  value, bid, hand[0], 'Four of a kind')
            if two == 2:                    return (hand_type_dict['Full house'],      value, bid, hand[0], 'Full house')
            if two == 1:                    return (hand_type_dict['Three of a kind'], value, bid, hand[0], 'Three of a kind')
            return (hand_type_dict['One pair'], value, bid, hand[0], 'One pair')
        case 2: # AAAJJ, AABJJ, ABCJJ
            if three == 1:                  return (hand_type_dict['Five of a kind'],  value, bid, hand[0], 'Five of a kind')
            if two == 2:                    return (hand_type_dict['Four of a kind'],  value, bid, hand[0], 'Four of a kind')
            return (hand_type_dict['Three of a kind'], value, bid, hand[0], 'Three of a kind')
        case 3: # AAJJJ, ABJJJ
            if two == 1:                    return (hand_type_dict['Five of a kind'],  value, bid, hand[0], 'Five of a kind')
            return (hand_type_dict['Four of a kind'],  value, bid, hand[0], 'Four of a kind')
        case 4: # AJJJJ
            return (hand_type_dict['Five of a kind'],  value, bid, hand[0], 'Five of a kind')
        case 5:
            return (hand_type_dict['Five of a kind'],  value, bid, hand[0], 'Five of a kind')

evaluated_hands = []
for hand in input:
    evaluated_hands.append(hand_eval(hand))    

evaluated_hands.sort()
total_winnings = 0
for i in range(len(evaluated_hands)):
    rank = i+1
    #print(rank, ':', evaluated_hands[i][2], evaluated_hands[i])
    total_winnings += rank*evaluated_hands[i][2]

print(total_winnings)

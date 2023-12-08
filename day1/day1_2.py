input = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']
numbers = {'one':'1XX', 'two':'2XX', 'three':'3XXXX', 'four':'4XXX', 'five':'5XXX', 'six':'6XX', 'seven':'7XXXX', 'eight':'8XXXX', 'nine':'9XXX'}
reverse_numbers = {'eno':'XX1', 'owt':'XX2', 'eerht':'XXXX3', 'ruof':'XXX4', 'evif':'XXX5', 'xis':'XX6', 'neves':'XXXX7', 'thgie':'XXXX8', 'enin':'XXX9'}
f = open('day1/day1_1.txt', 'r')
input = f.readlines()

def str_change_char(s, pos, c):
    return s[0:pos] + c[0] + s[pos+1:]

out = []
for line in input:    
    s = line.strip()
    s_reverse = line.strip()[::-1]
  
    for i in range(len(s)):
        ss = s[i: i+5]        
        for n in numbers.keys():
            ss = ss.replace(n, numbers[n])
        for j in range(len(ss)):            
            s = str_change_char(s, i+j, ss[j])

    for i in range(len(s_reverse)):
        ss = s_reverse[i: i+5]        
        for n in reverse_numbers.keys():
            ss = ss.replace(n, reverse_numbers[n])
        for j in range(len(ss)):            
            s_reverse = str_change_char(s_reverse, i+j, ss[j])

    s2 = ''
    for chr in s:
        if chr.isnumeric():
            s2 += chr
            break
    for chr in s_reverse:
        if chr.isnumeric():
            s2 += chr
            break
  
    if len(s2) == 1:
        s2 += s2
    
    out.append(s2)

sum = 0
for s in out:
    sum += int(s)

print(sum)


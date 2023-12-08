input = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
f = open('day1/day1_1.txt', 'r')
input = f.readlines()

out = []
for line in input:
    s = ''    
    for chr in line:
        if chr.isnumeric():
            s += chr
    if len(s) == 1:
        s += s
    else:
        s = s[0] + s[len(s)-1]    
    out.append(s)

sum = 0
for s in out:
    sum += int(s)

print(sum)





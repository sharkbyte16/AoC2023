next = []
i = 0
while True:
    for node in start:
        next.append(nodes[node][directions[i % len(directions)]])
    i += 1    
    sum = 0     # count non-Z-ending, if 0 than all are z-ending
    for node in next:
        if node[2] != 'Z':
            sum += 1            
    if sum < 1:        
        break
    start = next.copy()
    next = []
print('steps', i)
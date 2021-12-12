def advent11():
    count = 0
    l = []
    f = open('/Users/omkudtarkar/Documents/Code/files/Advent-1', 'r')
    for i in f:
        l.append(i)
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            count += 1
    f.close()
    return count + 1

def advent12():
    count = 0
    l = [int(x) for x in open('/Users/omkudtarkar/Documents/Code/files/Advent-1')]
    for i in range(3, len(l)):
        if ((l[i] + l[i-1] + l[i-2]) > (l[i-1] + l[i-2] + l[i-3])):
            count += 1
    return count
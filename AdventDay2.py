def advent21():
    l = []
    with open('/Users/omkudtarkar/Documents/Code/files/Advent-2') as f:
        l = f.readlines()
    a = []
    for i in l:
        a.append(i.split())
    d = {'forward': 0, 'depth': 0}
    for i in a:
        if i[0] == 'forward':
            d['forward'] += int(i[1])
        elif i[0] == 'down':
            d['depth'] += int(i[1])
        elif i[0] == 'up':
            d['depth'] -= int(i[1])
    return(d['forward'] * d['depth'])

def advent22():
    a = []
    with open('/Users/omkudtarkar/Documents/Code/files/Advent-2') as f:
        a = f.readlines()
    l = []
    for i in a:
        l.append(i.split())
    d = {'forward': 0, 'depth': 0, 'aim' : 0}
    x = [('forward', 5), ('down', 5), ('forward', 8), ('up', 3), ('down', 8), ('forward', 2)]
    for i in l:
        if i[0] == 'forward':
            d['forward'] += int(i[1])
            d['depth'] += (d['aim'] * int(i[1]))
        elif i[0] == 'down':
            d['aim'] += int(i[1])
        elif i[0] == 'up':
            d['aim'] -= int(i[1])
    return(d['forward'] * d['depth'])
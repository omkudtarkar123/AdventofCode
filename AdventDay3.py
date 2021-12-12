def advent31():
    l = [list(x) for x in open('/Users/omkudtarkar/Documents/Code/files/Advent-3')]
    # Adding comment here
    for i in l:
        if '\n' in i:
            i.remove('\n')
    d = {}
    a = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    gamma_rate = []
    epsilon_rate = []
    for j in range(len(l[0])):
        for i in l:
            if j not in d and i[j] == '1':
                d[j] = 1
            elif j in d and i[j] == '1':
                d[j] += 1
    for i in d:
        if d[i] > len(l)/2:
            gamma_rate.append('1')
            epsilon_rate.append('0')
        else:
            gamma_rate.append('0')
            epsilon_rate.append('1')
    return(int(''.join(gamma_rate),2) * int(''.join(epsilon_rate),2))

def advent32():
    l = [list(x) for x in open('/Users/omkudtarkar/Documents/Code/files/Advent-3')]
    for i in l:
        if '\n' in i:
            i.remove('\n')
    a = l[:]
    b = []
    oxygen_generator_rate = []
    num = 0
    for i in range(len(l[0])):
        if len(a) == 1:
            oxygen_generator_rate = a[:]
            break
        count = 0
        for j in a:
            if j[i] == '1':
                count += 1
        if count >= float(len(a))/2:
            num = 1
        else:
            num = 0
        oxygen_generator_rate.append(num)
        for k in a:
            if k[i] == str(num):
                b.append(k)
        a = []
        a = b[:]
        b = []
    
    c = l[:]
    d = []
    co_scraper_rate = []
    num = 0
    for i in range(len(l[0])):
        count = 0
        if len(c) == 1:
            co_scraper_rate = c[:]
            break
        for j in c:
            if j[i] == '0':
                count += 1
        if count <= float(len(c))/2:
            num = 0
        else:
            num = 1
        co_scraper_rate.append(num)
        for k in c:
            if k[i] == str(num):
                d.append(k)
        c = []
        c = d[:]
        d = []
    return(int(''.join(co_scraper_rate),2) * int(''.join(oxygen_generator_rate),2))

from collections import defaultdict

def advent41():
    with open("InputFiles/Advent-4") as textFile:
        lines = [line.split() for line in textFile]
    for i in lines:
        if [] in lines:
            lines.remove([])
    input = [46,79,77,45,57,34,44,13,32,88,86,82,91,97,89,1,48,31,18,10,55,74,24,11,80,78,28,37,47,17,21,61,26,85,99,96,23,70,3,54,5,41,50,63,14,64,42,36,95,52,76,68,29,9,98,35,84,83,71,49,73,58,56,66,92,30,51,20,81,69,65,15,6,16,39,43,67,7,59,40,60,4,90,72,22,0,93,94,38,53,87,27,12,2,25,19,8,62,33,75]
    l = []
    a = []
    c = {}
    r = {}
    boardnum = 10000
    sublist = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
    for i in range(len(lines)):
        if (i+1)%5 == 0:
            a.append(lines[i])
            l.append(a)
            a = []
            c[((i+1)/5)-1] = []
            r[((i+1)/5)-1] = []
        else:
            a.append(lines[i])
    for x in input:
        for i in l:
            for j in i:
                for k in j:
                    z = []
                    if int(k) == int(x):
                        c[l.index(i)].append(j.index(k))
                        r[l.index(i)].append((5*i.index(j)) + j.index(k))
                        #r[l.index(i)].sort()
        for d in c:
            for e in c[d]:
                if c[d].count(e) == 5:
                    if boardnum == 10000:
                        boardnum = d
        for d in r:
            for e in sublist:
                if (all(x in r[d] for x in e)):
                    if boardnum == 10000:
                        boardnum = d
                        print(r[60])
    #print(r[60])
    #print(boardnum)
    #print(l[boardnum][])
    #print(19+85+36+73+71+65+62+14+52+3+30+83+41+5+15+0+61+95)

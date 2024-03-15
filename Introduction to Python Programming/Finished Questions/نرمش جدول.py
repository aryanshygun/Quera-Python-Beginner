# https://quera.org/problemset/3413


def do_90():
    global xlist
    xlist_temp = list()
    for i in range(n):
        row = list()
        for j in range(-1, -n - 1, -1):
            row.append(xlist[j][i])
        xlist_temp.append(row)
    xlist = xlist_temp
    return xlist

def do_h():
    global xlist
    xlist_temp = list()
    for i in range(-1, -n - 1, -1):
        xlist_temp.append(xlist[i])
    xlist = xlist_temp
    return xlist

def do_v():
    global xlist
    xlist_temp = list()
    for i in range(n):
        row = list()
        for j in range(-1, -n - 1, -1):
            row.append(xlist[i][j])
        xlist_temp.append(row)
    xlist = xlist_temp
    return xlist
            
            
n = int(input())
xlist = list()
for i in range(n):
    x = str(input())
    xx = list()
    for i in x:
        xx.append(i)
    xlist.append(xx)
q = int(input())
for i in range(q):
    t = str(input())
    if t == '90':
        do_90()
    if t == 'V':
        do_v()
    if t == 'H':
        do_h()
        
        
for i in xlist:
    for j in i:
        print(j, end='')
    print()

 
        
        
# n = 2
# n = 3
# xlist = [['b', 'w', 'b'], ['w', 'w', 'w'], ['w', 'w', 'b']]
# xlist = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
# xlist = [['a', 'b'],['c', 'd']]
            
# do_90()
# do_v()
# do_h()

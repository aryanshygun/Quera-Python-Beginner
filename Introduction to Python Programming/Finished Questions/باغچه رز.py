# https://quera.org/college/12547/chapter/46830/lesson/168521/?comments_page=1&comments_filter=ALL

m, n = map(int, input().split())
xlist = []
for i in range(n):
    x = input()
    xlist.append(x)
    
xdict = {}
# m, n = 3, 2
# xlist = ['WBW', 'BBW']
ylist = []

for i in range(len(xlist)):
    yy = []
    for j in xlist[i]:
        if j == 'W':
            yy.append(1)
        else:
            yy.append(0)
    ylist.append(yy)
    result = [sum(values) for values in zip(*ylist)]

for i in result:
    if i % 2 == 0:
        print('B', end='')
    else:
        print('F', end='')
    
# print(result)

import math


qty = int(input())
xlist = []
for i in range(qty):
    name = input()
    k = list(map(float, input().split()))
    kol = 0
    for i in range(1, len(k)):
        kol += k[i]
    score = math.floor(kol / k[0])
    l = list(input().split())
    sport = int(l[0])
    xlist.append([name, score, sport])

xlist.sort(key=lambda x:(x[1], x[2]), reverse= True)

for i in xlist:
    print(i[0])
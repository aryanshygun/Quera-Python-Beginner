# https://quera.org/problemset/80651

xlist=[]

for _ in range(6):
    x = int(input())
    xlist.append(x)

team1 = min(xlist[0],xlist[1])
team2 = min(xlist[2],xlist[3])
team3 = min(xlist[4],xlist[5])

print(team1+team2+team3)
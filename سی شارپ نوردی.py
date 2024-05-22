# https://quera.org/problemset/170059
xlist = []

for i in range(2):
    a = int(input())
    xlist.append(a)
    
x, y = xlist[0], xlist[1]

z = abs(x - y)

if z == 0:
    print("0")
elif z == 1 and ( x + y == 3 or x + y == 7):
    print("1")
elif z == 1 and ( x + y == 5):
    print("2")
elif z == 2:
    print("1")
else:
    print("2")
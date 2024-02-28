# https://quera.org/problemset/308

n = int(input())
xy = []

for i in range(n):
    q = list(map(int, input().split()))
    xy.append(q)

print(xy)

xmax = max(xy, key=lambda t: t[0])[0]
ymax = max(xy, key=lambda t: t[1])[1]

print(xmax, ymax)

x = []

# for i in range(0, xmax):
#     if i % 2 == 0:
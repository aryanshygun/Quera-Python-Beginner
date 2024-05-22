# https://quera.org/problemset/10163
a, b, c = map(int, input().split())

x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())
z1, z2 = map(int, input().split())

x = [i for i in range(x1, x2)]
y = [i for i in range(y1, y2)]
z = [i for i in range(z1, z2)]

# print(x)
# print(y)
# print(z)

whole = list()
whole.extend(x)
whole.extend(y)
whole.extend(z)
whole.sort()
# print(whole)

length = whole[-1]
# print(length)


xdic = {}
for i in whole:
    if i in xdic:
        xdic[i] += 1
    else:
        xdic[i] = 1
# print(xdic)
p1 = 0
p2 = 0
p3 = 0
for i, j in xdic.items():
    # print(i, j)
    if j == 1:
        p1 += 1
    if j == 2:
        p2 += 1
    if j == 3:
        p3 += 1
   
# print(p1, p2, p3)
   
x = p1*1*a + p2*2*b + p3*3*c
print(x)
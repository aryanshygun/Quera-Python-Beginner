n = int(input())
xlist = []
for i in range(n):
    x = input()
    xx = []
    for i in x:
        xx.append(i)
    xx = set(xx)
    xx = list(xx)
    xlist.append(xx)
for i in range(len(xlist)):
    for j in range(len(xlist[i])):
        xlist.pop(i)
        xlist.insert(i, j+1)
# print(xlist)
print(max(xlist))
# print(len(max(xlist)))
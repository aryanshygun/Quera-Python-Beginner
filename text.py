n, k = 4,7
# xlist = []
# for i in range(1, n + 1):
#     xlist.append(i)
#     xlist.append(i)

xlist = [1, 1, 2, 2, 3, 3, 4, 4]
# xlist = [1,2,3,4]
ylist = []

i = 0
p = k
# while i < 7:
while xlist:
    u = i % len(xlist)
    ylist.extend(xlist)
    if p / k == 1:
        xlist.pop()
        # ylist.pop()
        p +=1
    else:
        i += 1
        p += 1
print(len(ylist))
        
        
for i in range(0, len(ylist), k):
    print(*ylist[i:i+k])
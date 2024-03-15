x = str(input())
y = 0
for i in x:
    i = int(i)
    y += i

x = int(x)

# print('x', x)
# print('y', y)



ylist = []
x += 1

while len(ylist) < y:
    z = 0
    for i in range(1,x + 1):
        if x % i == 0:
            z += 1
    # print('x',x,'z',z)
    if z == 2:
        # print('yessir')
        ylist.append(x)
        # print('ylist', ylist)
        x += 1
    elif z != 2:
        x +=1
        # print('nope')




print(ylist[y-1])
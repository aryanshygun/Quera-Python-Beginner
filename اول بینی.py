# https://quera.org/college/12547/chapter/46830/lesson/168515/?comments_page=1&comments_filter=ALL



x = int(input())
y = int(input())
tlist = []
# x = 4
# y = 10
for i in range(x + 1, y):
    z = 0
    for j in range(1, i):
        if i  % j == 0:
            z += 1
    if z == 1:
        tlist.append(i)
        
# print(tlist)

xx = ','.join(map(str, tlist))

print(xx)
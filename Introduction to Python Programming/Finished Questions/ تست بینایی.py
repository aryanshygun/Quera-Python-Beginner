# https://quera.org/college/12547/chapter/46830/lesson/168506/?comments_page=1&comments_filter=ALL

x = int(input())
y = str(input())
z = str(input())
a = 0
for i in  range(len(z)):
    if z[i] != y[i]:
        a += 1 
    
print(a)

# https://quera.org/college/12547/chapter/46830/lesson/168519/?comments_page=1&comments_filter=ALL

def tekrar(n):
    xdict = {}
    for o in n:
        if o in xdict:
            xdict[o] += 1
        else:
            xdict[o] = 1
    for x, y in xdict.items():
        if y >= 4:
            return True
            
def motev(n):
    for i in range(0, len(n)-2):
        
        if n[i] == n[i+1] and n[i] == n[i+2]:
            return True
        
def pal(n):
    if n == n[::-1]:
        return True


n = int(input())
xlist = []
for i in range(n):
    x = str(input())
    xlist.append(x)

for i in xlist:    
    if pal(i) == True or tekrar(i) == True or motev(i) == True:
        print('Ronde!')
    else:
        print('Rond Nist')
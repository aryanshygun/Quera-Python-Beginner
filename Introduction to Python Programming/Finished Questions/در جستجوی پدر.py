# https://quera.org/college/12547/chapter/46830/lesson/168507/?comments_page=1&comments_filter=ALL

def addit(n):
    n = str(n)
    x = 0
    for i in n:
        i = int(i)
        x += i 
    return x

def prime_factors(n):
    factors = []
    adad = 2
    while n > 1:
        while n % adad == 0:
            factors.append(adad)
            n = n // adad
        adad += 1
    y = 0
    for i in set(factors):
        y += i
    return y
    
def pedar(n):
    jamragham = addit(n)
    jamprime = prime_factors(n)
    return jamragham + jamprime + n



tedad = int(input())
emha = []
for i in range(tedad):
    m = int(input())
    emha.append(m)

# print('emha', emha)

# emha = [4, 20, 24]

for i in emha: 
    avallist = []
    for j in range(i):
        x = pedar(j)
        avallist.append(x)
    if i in avallist:
        print('Yes')
    else:
        print('No')
        
    
# num = int(input())


# avallist = []


# for i in range(num):
#     x = pedar(i)
#     # print(pedar(i))
#     avallist.append(x)

# print(avallist)


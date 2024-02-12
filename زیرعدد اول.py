num = 5





def superprime(x):
    num_zir = []
    zarb = 1
    zir = x // zarb
    
    while zir != 0:
        num_zir.insert(0, zir)
        zarb *= 10
        zir = x // zarb
    print(num_zir)
    # return num_zir
    
def is_prime(x):
    p = 0
    for i in num_zir:
        v = 0
        for j in range(i,i+1):
            if i % j == 0:
                v += 1
        if v == 2:
            p +=1
            

y = 0
q = 1
while y != num:
    z = 0
    for i in range(1, q + 1):
        if q % i == 0:
            z += 1
    if z == 2:
        y +=1
    
print(y)
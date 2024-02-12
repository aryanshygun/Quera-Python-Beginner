turn = 10
superprimes = []

zir_num = []
primes = []
natural = []
l = 0
num = 1

while len(superprimes) != turn:
    new = 0
    l += 1
    for i in range(num, num + 1):
        v = 0
        for j in range(1, i + 1):
            if i % j == 0:
                v +=1
        if v == 2:
            zprime = i
        else:
            continue
        
        
        
        each_zir_num = []
        
        q = 1
        qq = zprime // q

        while qq != 0:
            each_zir_num.append(qq)
            q *= 10
            qq = zprime // q
        zir_num.append(each_zir_num)
        
    num += 1
    
    if len(zir_num) > 0:
        superprimes.append(zir_num[-1])
        if len(superprimes) > 2:
            if superprimes[-1] == superprimes[-2]:
                superprimes.pop()
            # print('huh', superprimes)
    
    # superprimes.append(l)
    


print('Complete Superprimes =', superprimes)

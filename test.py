turn = 15
superprimes = []

zir_num = []
primes = []
natural = []
l = 0
num = 1

while len(superprimes) != turn:
    l += 1
    prime_num = 0
    for i in range(num, num + 1):
        v = 0
        for j in range(1, i + 1):
            if i % j == 0:
                v +=1
        if v == 2:
            primes.append(i)
            prime_num = str(i)
        else:
            continue
        
        
        print('primes', primes)
        
        
        each_zir_num = []
        for prime in prime_num:
            prime = int(prime_num)
            print('prime', prime)
            q = 1
            qq = prime // q
            # each_zir_num = []
            while qq != 0:
                each_zir_num.append(prime)
                q *= 10
                qq = prime // q
        zir_num.append(each_zir_num)
        print('zir num', zir_num)
        
        
        
        
        # q = 1
        # qq = i // q
        # each_zir_num = []
        # print('i =', i)
        # print('num =', num)
        # while qq != 0:
        #     each_zir_num.append(qq)
        #     q *= 10
        #     qq = i // q
        # zir_num.append(each_zir_num)
        
        # print('each_zir_num =', each_zir_num)
        # print('zir_num =', zir_num)
    num += 1
    
    
    
    
    
    
    
    
    
    
    superprimes.append(l)
    print('Superprimes =', superprimes)
    print()
    
print('Complete Superprimes =', superprimes)
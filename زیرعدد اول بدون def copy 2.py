turn = 30
superprimes = []

zir_num = []

natural = []
l = 0
num = 1

while len(superprimes) != turn:
    l += 1
    
    for i in range(num, num + 1):
        q = 1
        qq = i // q
        each_zir_num = []
        print('i =', i)
        print('num =', num)
        while qq != 0:
            each_zir_num.append(qq)
            q *= 10
            qq = i // q
        zir_num.append(each_zir_num)
        
        print('each_zir_num =', each_zir_num)
        print('zir_num =', zir_num)
    num += 1
    
    
    
    
    
    
    
    
    
    
    superprimes.append(l)
    print('Superprimes =', superprimes)
    print()
    
print('Complete Superprimes =', superprimes)
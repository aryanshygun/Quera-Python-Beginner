# https://quera.org/problemset/298
# import time


n =int(input())
# n = 100

# start_time = time.time()


def is_prime(x):
    v = 0
    for i in range(1, x +1 ):
        if x % i == 0:
            v += 1
    if v == 2:
        return True
    else:
        return False
    
    
primes = []
for i in range(1, n + 1):
    if is_prime(i) == True:
        primes.append(i)
   


zarb = []   
while n != 1:
    for i in primes:
        x = 0
        while n % i == 0:
            x += 1
            n /= i
        if x != 0:
            if x == 1:
                u = f'{i}'
                zarb.append(u)
            else:
                u = f'{i}^{x}'
                zarb.append(u)

for i in zarb:
    if i == zarb[-1]:
        print(i)
    else:
        print(i, end='*')
        
for _ in range(1000000):
    pass

# end_time = time.time()

# elapsed_time = end_time-start_time

# print('elapsed time',elapsed_time)
# https://quera.org/problemset/12912

import itertools

def sub(n):
    subnets = []
    
    for r in range(n + 1):
        for i in itertools.combinations(range(1, n + 1), r):
            subnets.append(set(i))
    return subnets

n = int(input())
# print(sub(n))
for i in range(len(sub(n))):
    if i == 0:
        print('{}')
    else:
        print(sub(n)[i])
        
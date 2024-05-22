turn = 5000

superprimes = []
candidprimes = []
supersuperprimes = []
zir_num = []

def is_prime(y):
    
    p = 0
    v = 0
    for j in range(1, y +1):
        if y % j == 0:
            
            v +=1

    if v == 2:
        p +=1
    return p

l = 0
num = 1

vnum = int(input())
while len(superprimes) != turn:
    each_zir_num = []
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
        
        q = 1
        qq = zprime // q
        while qq != 0:
            each_zir_num.append(qq)
            q *= 10
            qq = zprime // q
        zir_num.append(each_zir_num)
        
    num += 1
    
    if len(zir_num) > 0:
        candidprimes.append(zir_num[-1])
        if len(candidprimes) > 2:
            if candidprimes[-1] == candidprimes[-2]:
                candidprimes.pop()

    superprimes.append(l)

final = []


for i in candidprimes:
    if len(i) == 1:
        final.append(i)
    elif len(i) > 1:
        
        x = 1
        for y in i[1::]:

            if is_prime(y) == 1:
                x += 1

                if len(i) == x:
                    final.append(i)
                else:
                    continue

finall= []
for i in final:
    finall.append(i[0])

print(finall[vnum-1])
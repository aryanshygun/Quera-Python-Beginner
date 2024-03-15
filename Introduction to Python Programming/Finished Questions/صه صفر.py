def binn(n):
    
    xlist = []
    for i in range(2**n):
        xlist.append(bin(i)[2:].zfill(n))
        
    x = 0
    for i in xlist:
        if '000' in i:
            continue
        else:
            x += 1
    return x


n = int(input())
print(binn(n))

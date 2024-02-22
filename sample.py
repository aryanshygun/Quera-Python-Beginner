xdict = {}

x = input()
while x!= 'End':
    a, b = x.split()
    b = float(b)
    xdict[a] = b
    x = input()
# print(xdict)

whole = 0
n = 0
for j in xdict.values():
    whole += j
    n +=1
avg = whole / n
# print(avg)


selected = []
for i, j in xdict.items():
    if j >= avg:
        selected.append(i)
    
        
print(selected)

whole2 = 0
n2 = 0

for i in selected:
    n2 +=1
    whole2 += xdict[i]
# print('who', whole2)
avg2 = whole2 / n2
print(avg2)
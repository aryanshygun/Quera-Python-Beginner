xlist = [1,1,3,4,2,2,4]

xdict ={}
for i in xlist:
    xdict[i] = xdict.get(i, 0) + 1
    
print(xdict)
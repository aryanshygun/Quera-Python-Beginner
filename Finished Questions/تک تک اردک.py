def tak(x, xlist):
    if len(xlist) == 1:
        return xlist[0]
    else:
        ylist = []
        count = x % 2
        for i in range(count, len(xlist), 2):
            ylist.append(xlist[i])
            
        if (len(xlist)) / len(ylist) == 2:
            xlist = ylist
            return tak(x, xlist)
        else:
            x += 1
            xlist = ylist
            return tak(x, xlist)
    
    
    
n = int(input())
xlist = []
for i in range(n):
    xlist.append(i + 1)
    
x = 0
print(tak(x, xlist))





# quera solution

# def solve(k):
#     if k == 1:
#         return 1
#     elif k % 2 == 0:
#         return 2 * solve(k / 2) - 1
#     else:
#         return 2 * solve((k - 1) / 2) + 1

# n = int(input())
# print(solve(n))
# https://quera.org/college/3078/chapter/8408/lesson/29921/?comments_page=1&comments_filter=ALL&submissions_page=1

n = int(input())
k = str(input())
nlist = []
for i in range(n):
    nlist.append(input())
    
# n = 3
# k = '123'
# nlist = ['241356789', '987546231', '956874231']


xcomp = 0

for i in range(len(nlist)):
    # x = 0
    # if nlist[i] == k[i]:
    #     pass
    # else:
    x1temp = 0
    for j in range(len(nlist[i])):
        if nlist[i][j] != k[i]:
            x1temp += 1
        else:
            break
    x2temp = 0
    for j in range(len(nlist[i])):
        if nlist[i][-j] != k[i]:
            x2temp += 1
        else:
            break
    # x = min(x1temp, x2temp)
    xcomp += min(x1temp, x2temp)

print(xcomp)
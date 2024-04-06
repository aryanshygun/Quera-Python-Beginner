
# n = int(input())
# xlist = list(map(int, input().split()))

n = 8
xlist = [1, 9, 8, 7, 5, 3, 2, 4]

xmax = xlist.index(max(xlist))


def soma(x, xlist):
    if xlist == sorted(xlist) or xlist == sorted(xlist, reverse=True):
        return 'Yes'
    q = xlist[x]
    w = xlist[x::]
    e = min(w)
    if q == e:
        return 'Yes'
    for i in range(x + 1, len(xlist) - 1):
        if xlist[i] > xlist[i+1]:
            return soma(x + 1, xlist)
        else:
            return 'No'            

print(soma(xmax, xlist))

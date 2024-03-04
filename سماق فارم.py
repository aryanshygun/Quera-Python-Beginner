# https://quera.org/college/12547/chapter/46830/lesson/168509/?comments_page=1&comments_filter=ALL


# n = int(input())
# xlist = list(map(int, input().split()))

n = 5
xlist = [1, 2, 4, 3, 1]

xmax = xlist.index(max(xlist))



print(soma(xmax, n))


def soma (xmax, xlist):
    if xmax = min(xlist):
        return 'Yes'
    for i in xlist[xmax::]:
        if i < xlist[xmax]:
            return soma(i, xlist)
        else:
            return 'No'
        
# print(soma(xmax, n))
    
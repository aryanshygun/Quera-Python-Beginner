# https://quera.org/college/12547/chapter/46830/lesson/168509/?comments_page=1&comments_filter=ALL


n = int(input())

xlist = list(map(int, input().split()))

# n = 8
# xlist = [1, 9, 8, 7, 5, 3, 2, 4]

xmax = xlist.index(max(xlist))


def soma(x, xlist):
    if xlist[x+1] == min(xlist[xmax::]):
        return 'Yes'
    for i in range(x + 1, len(xlist)-1):
        if xlist[i] >= xlist[i + 1]:
            return soma(x + 1, xlist)
        else:
            return 'No'            
            # print('No')

        # print(xlist[i]) 
        
print(soma(xmax, xlist))

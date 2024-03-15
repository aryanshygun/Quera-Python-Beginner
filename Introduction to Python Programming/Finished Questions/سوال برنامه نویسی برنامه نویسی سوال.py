# https://quera.org/problemset/3408

n = int(input())

xlist = list(map(str, input().split()))

for i in range(1, n + 1):
    print(xlist[-i], end= ' ')
# https://quera.org/problemset/127289

n = int(input())
x = 'codecup6'

xlen = len(x)

if n <= xlen:
    print(x[n-1])
else:
    n = n % xlen
    print(x[n-1])
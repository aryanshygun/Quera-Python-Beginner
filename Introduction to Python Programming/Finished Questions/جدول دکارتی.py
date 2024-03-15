# https://quera.org/problemset/209103

n, m = map(int, input().split())
# n = 3
# m = 4

# n = 'satr'
# m = 'sotun'

nreal = 2*n + 1
mreal = 2*n + 1



for i in range(1, nreal + 1):
    if i % 2 != 0:
        print(' _'*m)
    elif i % 2 == 0:
        print('| '*(m + 1))
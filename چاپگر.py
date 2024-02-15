# https://quera.org/problemset/64434

n, m = map(int, input().split())

x = n * 3
y = m * 3

for i in range(x):
    for j in range(y):
        if j < ( y / 3):
            if i < (x / 3):
                print('X', end = '')
            elif i >= (x / 3) and i < ( (2 * x) / 3) :
                print('.', end = '')
            else:
                print('X', end = '')
                
        elif j >= (y / 3) and j < ( (2 * y) / 3) :
            if i < (x / 3):
                print('.', end = '')
            elif i >= (x / 3) and i < ( (2 * x) / 3) :
                print('X', end = '')
            else:
                print('.', end = '')
        
        else:
            if i < (x / 3):
                print('X', end = '')
            elif i >= (x / 3) and i < ( (2 * x) / 3) :
                print('.', end = '')
            else:
                print('X', end = '')
    print()
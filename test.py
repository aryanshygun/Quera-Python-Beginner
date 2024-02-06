n = int(input())

sum=0
for i in range(1, n+1):
    z= 0
    for j in range(1,i+1):
        z +=j
        print(j, end='')
        if j < i :
            print('+', end='')
    print(' =',z)
    sum +=z

print('Total sum of series is:',sum)

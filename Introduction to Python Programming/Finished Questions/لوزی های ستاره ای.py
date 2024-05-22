# https://quera.org/problemset/9773?tab=description
qty = int(input())
line = qty // 2 + 1
for i in range(1, line+1):
    print(' '*(line - i)+"*"*(2*i-1)+' '*(line - i)+' '*(line - i)+"*"*(2*i-1))
    
for i in range(line, 0, -1):
    print(' '*(line-i+1)+"*"*(2*i-3)+' '*(line-i+1)+' '*(line-i+1)+"*"*(2*i-3))

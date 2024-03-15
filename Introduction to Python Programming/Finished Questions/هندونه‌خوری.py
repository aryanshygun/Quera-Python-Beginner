# https://quera.org/problemset/35253

 
n = int(input())

ans = tuple(map(int, input().split()))
a = []
for i in ans:
    a.append(i)
    
for i in range(0,len(a)-1):
    if a[0] < a[1]:
        a.remove(a[0])
        # print(a)
    else:
        a.remove(a[1])
        # print(a)
        
for i in range(1, len(ans)+1):
    if a[0] == ans[i-1]:
        print(i)

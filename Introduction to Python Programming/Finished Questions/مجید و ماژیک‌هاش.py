# https://quera.org/problemset/9109

n = int(input())

m = list(map(int, input().split()))

m.sort()
n = list(set(m))

count = {}
for i in m:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1


small = min(count.values())
smalll=[]


for i, j in count.items():
    if j == small:
        smalll.append(i)

print(min(smalll))
# https://quera.org/problemset/10166

k = [3,3,1,1,2,2]
n = [1,2,3]
s = [2,1,2,3]

t = int(input())
ans = list(map(int, input()))
xlist = []
# for i in ans:
    # xlist.append(i)

while len(k) < len(ans):
    k.extend(k)
while len(n) < len(ans):
    n.extend(n)
while len(s) < len(ans):
    s.extend(s)

kscore = 0
nscore = 0
sscore = 0

for i in range(len(ans)):
    if ans[i] == k[i]:
        kscore +=1
    if ans[i] == n[i]:
        nscore +=1
    if ans[i] == s[i]:
        sscore +=1

# print('kscore', kscore)
# print('nscore', nscore)
# print('sscore', sscore)

maxx = max(kscore, nscore, sscore)

print(maxx)
# print(maxx, type(maxx))
if kscore == maxx:
    print('keyvoon')
if nscore == maxx:
    print('nezam')
if sscore == maxx:
    print('shir farhad')

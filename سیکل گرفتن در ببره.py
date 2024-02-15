# https://quera.org/problemset/10166

k = [3,3,1,1,2,2]
n = [1,2,3]
s = [2,1,2,3]

t = int(input())
ans = str(input())
xlist = []
# for i in ans:
    # xlist.append(i)

while len(k) < len(ans):
    k.extend(k)
while len(n) < len(ans):
    n.extend(n)
while len(s) < len(ans):
    s.extend(s)

# kscore = 0
for i in ans:
    kscore = 0
    i = int(i)
    if ans[i] == k[i]:
        print('yea')
        kscore +=1


print(kscore)









# for i in ans:
#     i = int(i)
#     kscore = 0
#     for j in k:
#         # print(i, type(i))
#         # print(j, type(j))
#         if i == j:
#             kscore +=1

# nscore = 0
# for i in ans:
#     i = int(i)

#     for j in n:
#         if i == j:
#             nscore +=1
    
# sscore = 0   
# for i in ans:
#     i = int(i)

#     for j in s:
#         if i == j:
#             sscore +=1
            
# print('k',kscore)
# print('n', nscore)
# print('s', sscore)
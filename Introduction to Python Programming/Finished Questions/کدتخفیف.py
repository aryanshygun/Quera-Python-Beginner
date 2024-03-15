# https://quera.org/problemset/10327
# n, t = input().split()
# n = int(n)

# entries = []
# for i in range(n):
#     x = input()
#     x = list(set(x))
#     entries.append(x)

# tletter = []
# for i in t:
#     tletter.append(i)


# for i in entries:
#     v = 0
#     for j in i:
#         for k in tletter:
#             if j == k:
#                 v +=1
#     if len(t) == v:
#         print('Yes')
#     else:
#         print('No')



inp = input().split()
n = int(inp[0])
basecode = set(inp[1])
codes = []
for _ in range(n):
    codes.append(input())
for code in codes:
    if set(code) == basecode:
        print('Yes')
    else:
        print('No')
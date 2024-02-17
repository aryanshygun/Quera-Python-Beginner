# https://quera.org/problemset/28948
import time
from time import process_time
# ans = str(input())
# x = []

# for i in ans:
#     x.append(i)

# for i in range(len(x)):
#     if x[0] == '=':
#         x.pop(0)
#     else:
#         break
# print(x)



x = ['t', 'e', 's', 't', 't', 'w', 'o', 'o', '=', '=', '=', 'w', 'o']


print()
print(process_time())
y = []
for i in range(len(x)):
    if x[i] != '=':
        y.append(x[i])
    if x[i] == '=':
        y.pop()
print()
print(process_time())
for i in y:
    print(i, end='')
print()
print(process_time())
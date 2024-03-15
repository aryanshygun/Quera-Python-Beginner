# https://quera.org/problemset/308


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']








x = str(input())
x = x.lower()

xlist = []

for i in x:
    if i in letters:
        xlist.append(i)

xcheck = ''.join(map(str, xlist))
  
# print(xcheck)
# print(xcheck[::-1])


if xcheck == xcheck[::-1]:
    print('YES')
else:
    print('NO')

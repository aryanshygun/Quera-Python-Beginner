# https://quera.org/problemset/34081

x, y = map(int, input().split())
# x, y = 5, 2

# a = 1
# z = x % a
# q = 0
# print('z',z)
# while z != 0:
#     a += y
#     q += 1
    

# print('a',a)
# print('q',q)
# print('z',z)





a = 1 + y
b = 1
z = a % x

while z != 1:
    # z = a % x
    a = a + y
    z = a % x
    b += 1
    # print('a',a)
    # print('z',z)
    # print()

# print('z8', z)
# print('b', b)
print(b)
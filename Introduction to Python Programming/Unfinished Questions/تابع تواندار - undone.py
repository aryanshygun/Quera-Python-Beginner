# https://quera.org/problemset/304

base = float(input())
exp = float(input())

# base = 2
# exp = 3
# z = 0
# def mypow(x, y, z):
#     # z = 0
#     if z == y:
#         return x
#     return mypow(x*x, y, z + 1)

# print(mypow(base, exp, z))

# x = pow(base, exp)
x = base ** exp
x = format(x, '.3f')
print(x)
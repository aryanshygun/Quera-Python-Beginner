# https://quera.org/problemset/283

a = int(input())
b = int(input())



if a <= b:
    print("Wrong order!")
elif (a - b) % 2 != 0:
    print("Wrong difference!")
else:
    c = a - b
    ro_zir = ("* " * a + "\n") * (c // 2)
    vasat = ("* " * (c // 2) + "  " * b + "* " * (c // 2) + "\n") * b
    print(f'{ro_zir}{vasat}{ro_zir[:-1]}')
# https://quera.org/problemset/617


num = int(input())

num_check = str(num)
num_check = num_check[::-1]
num_check = int(num_check)

if num == num_check:
    print('YES')
else:
    print('NO')

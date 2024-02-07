# https://quera.org/problemset/6375?tab=description

a, b, c = map(int, input().split())

if a == b == c:
    print(0)
else:
    mid = (a + b + c) / 3.0
    if a == mid or b == mid or c == mid:
        print(1)
    else:
        print(2)

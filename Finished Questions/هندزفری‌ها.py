# https://quera.org/problemset/110014

a, b = map(str, input().split())
c, d = map(str, input().split())

a = a.upper()
b = b.upper()
c = c.upper()
d = d.upper()

if a == b or c == d:
    print('YES')
elif a == d or b == c:
    print('YES')
else:
    print("NO")
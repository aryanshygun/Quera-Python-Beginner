# p, d = map(int, input().split())

p, d = 8, 7
y = int(p / 2)
x = d % p
# print(x)
while x not in range(0, y + 1):
    d += d
    x = d % p
print(d)
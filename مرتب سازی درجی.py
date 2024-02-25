a = [1, 15, 12, 13, 9, 5, 4, 2]

for j in range(len(a)):
    while j > 0 and a[j] < a[j - 1]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1

print(a)
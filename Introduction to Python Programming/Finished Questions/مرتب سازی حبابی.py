a = [3, 10, 12, 6, 8, 11]

for i in range(len(a)):
    for j in range(0, len(a) - i - 1):
        if a[j+1] < a[j]:
            a[j], a[j+1] = a[j+1], a[j]
            
print(a)
a = [5, 8, 1, 3, 2, 6]

for i in range(len(a)):
    min = i
    for j in range(i, len(a)):
        if a[j] < a[min]:
            min = j
    a[i], a[min] = a[min], a[i] 
print(a)
def binary_search(arr, x):
    if arr[-1] == x:
        return 1
    if arr[-1] < x:
        return 0
    low = -1
    high = len(arr) -1

    while high - low > 1:
        middle = (low + high) // 2
        if arr[middle] <= x:
            low = middle
        else:
            high = middle
    if arr[low] == x:
        return 1
    return 0












n, m = map(int, input().split())



arr = list(map(int, input().split()))
y = []

for i in range(m):
    a, b  = input().split()
    b = int(b)
    y.append(b)
    
# print()
# print('arr', arr)
# print('y', y)
# print()

for i in y:
    # print('i', i)
    print(binary_search(arr, i))


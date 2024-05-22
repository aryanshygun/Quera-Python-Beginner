def c(row, col):
    if col == 0:
        return 1
    if row == 0:
        return 0
    return c(row - 1, col) + c(row - 1, col - 1)


n = int(input())
for row in range(n):
    for col in range(row + 1):
        print(c(row, col), end=' ')
    print()
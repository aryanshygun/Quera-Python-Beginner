cnt = 0

def hanoi(start, finish, help, n):
    global cnt
    if n == 1:
        cnt += 1 
        print(cnt, start, finish)
        return
    hanoi(start, help, finish, n -1)
    cnt += 1
    print(cnt, start, finish)
    hanoi(help, finish, start, n - 1)

n = int(input())
hanoi('A', 'C', 'B', n)
# https://quera.org/problemset/31021

n = int(input())
people = list(map(str, input().split()))

coming = list()

# hello part
for i in range(len(people)):
    coming.insert(0, people[0])
    people.pop(0)
    
    for j in range(1, len(coming)):
        print(f'{coming[0]}: salam {coming[j]}!')

# going part
going = coming[::-1]
for i in range(len(going)):
    print(f'{going[0]}: khodafez bacheha!')
    for j in range(1, len(going)):
        print(f'{going[j]}: khodafez {going[0]}!')
    going.pop(0)

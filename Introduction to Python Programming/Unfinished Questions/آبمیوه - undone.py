# https://quera.org/contest/assignments/64031/problems/220995

n, vol = map(int, input().split())

drinks = []
for i in range(n):
    whole_value, qty = map(int, input().split())
    raw_value = whole_value / qty
    drinks.append([raw_value, qty])
drinks.sort(key= lambda item: item[1])

quality = 0

while vol > 0:
    for i in range(len(drinks)):
        j , k = drinks[i][0], drinks[i][1]
        if k > vol:
            k = vol
        else:
            pass
        vol -= k
        quality += j*k


print(round(quality, 1))

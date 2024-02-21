# https://quera.org/contest/assignments/64031/problems/220995

n, vol = map(int, input().split())

drinks = []
for i in range(n):
    whole_value, qty = map(int, input().split())
    raw_value = whole_value / qty
    drinks.append([raw_value, qty])
drinks.sort(key= lambda item: item[1])


quality = 0
while len(drinks) != 0:
    j , k = drinks[0][0], drinks[0][1]
    if k > vol:
        k = vol
    else:
        pass
    vol -= k
    quality += j*k
    drinks.pop(0)

print(round(quality, 1))

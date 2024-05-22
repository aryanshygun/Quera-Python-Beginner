# https://quera.org/problemset/6192?tab=description

a, b, c, d, e, f = map(int, input().split())

boxfloor = [a, b]
boxfloor.sort()

icefloor = [d, e, f]
y1 = max(d, e, f)
icefloor.remove(y1)
icefloor.sort()

if (icefloor[0] <= boxfloor[0]) and (icefloor[1] <= boxfloor[1]):
    print("zende mimuni")
else:
    print("dari mimiri")

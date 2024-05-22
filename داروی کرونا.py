# https://quera.org/problemset/178600

n = int(input())
k = int(input())
p = int(input())
q = int(input())

shek = n - k
nama = p - q

if shek > nama:
    print("Shekarestan")
elif shek < nama:
    print("Namakestan")
else:
    print("Equal")
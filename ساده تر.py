# https://quera.org/problemset/3403

xlist=[]

for _ in range(4):
    x = int(input())
    xlist.append(x)
    

a, b, c, d = xlist[0], xlist[1], xlist[2], xlist[3]

a, b, c, d = float(a), float(b), float(c), float(d)

sum = a + b + c + d
average = sum/4
product = a*b*c*d
max = max(a,b,c,d)
min = min(a,b,c,d)

# # print(a,b,c,d)
# print("Sum :", a+b+c+d)
# print("Average :",((a+b+c+d)/4))
# print("Product :",a*b*c*d)
# print("MAX :",max(a,b,c,d))
# print("MIN :",min(a,b,c,d))

print(f"Sum : {sum:04f}")
print(f"Average : {average:04f}")
print(f"Product : {product:04f}")
print(f"MAX : {max:04f}")
print(f"MIN : {min:04f}")
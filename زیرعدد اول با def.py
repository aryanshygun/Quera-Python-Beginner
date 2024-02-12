turn = 5

num_zir = []
list_fogh_aval = []
p = 0

def superprime(x):
    global num_zir
    zarb = 1
    zir = x // zarb
    
    while zir != 0:
        num_zir.insert(0, zir)
        zarb *= 10
        zir = x // zarb
    return num_zir



def is_prime(y):
    
    global p
    v = 0
    for j in range(1, y +1):
        if y % j == 0:
            
            v +=1

    if v == 2:
        p +=1
    return p



num = 1
while len(list_fogh_aval) != turn:
    for x in range(1, num + 1):
        superprime(x)
        for y in num_zir:
            is_prime(y)
        print('p',p)
        if len(num_zir) == p:
            list_fogh_aval.insert(0, num)
            num += 1
        else:
            num += 1

print(list_fogh_aval)

# num = 1
# while len(list_fogh_aval) != turn:
#     for i in range(1, num + 1):
#         x = i
#         superprime(x)
#         for j in num_zir:
#             y = j
#             is_prime(y)
#             if len(num_zir) == p:
#                 list_fogh_aval.insert(0, num)
#                 num += 1
#             else:
#                 num += 1

# print(list_fogh_aval)


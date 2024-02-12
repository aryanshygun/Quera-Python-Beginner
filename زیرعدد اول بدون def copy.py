turn = 5

list_superprime = []

num = 20
# zir_num = []

# while len(list_superprime) != turn:
#     for i in range(1, num + 1):
#         q = 1
#         qq = i // q
#         while qq != 0:
#             zir_num.insert(0, qq)
#             q *= 10
#             qq = i // q
#             print('how many qq')
#         print('zir_num', i, zir_num)
#         print()
    
#         p = 0
#         for j in zir_num:
#             v = 0
#             for k in range(1, j + 1):
#                 if j % k == 0:
#                     v += 1
#             if v == 2:
#                 p += 1
#         if p == len(zir_num):
#             list_superprime.append(i)
#     # list_superprime.append('huh')
#     print('list_supertime',list_superprime)
#     num += 1


# while len(list_superprime) != 5:
#     for i in range(1, 100):
#         q = 1
#         qq = i // q
#         while q != 0:
#             zir_num.insert(0, qq)
#             q *= 10
#             qq = i // q
zir_num = []
num = 1
while num != 10:
    
    for i in range(1, num + 1):
        
        q = 1
        qq = i // q
        each_zir_num = []
        
        while qq != 0:
            each_zir_num.append(qq)
            q *= 10
            qq = i // q
        zir_num.append(each_zir_num)
        
        print()
        
        for p in zir_num:
            # print(i, p)
            for h in p:
                print(i, h)
            # for j in i:
                # print(j)
    num += 1
        
# print(zir_num)
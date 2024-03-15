# #https://quera.org/problemset/209104

# print("\n--------------------------\n")

# # ans_list[0] = Haj
# # ans_list[1] = karbala
# # ans_list[2] = mashti
# ans = input("Enter Y/N\n").lower()

ans = input().lower()
ans_list = []

for i in ans:
    ans_list.append(i)

if ans_list[0] == 'y':
    print("Haji")
elif ans_list[1] == 'y':
    print("Karbalaee")
elif ans_list[2] == 'y':
    print("Mashti")
else:
    print("Agha")
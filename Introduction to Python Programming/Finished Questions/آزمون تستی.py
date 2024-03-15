# https://quera.org/problemset/148640

n = int(input())

key=[]
keyin = input()
keyin = keyin.upper()
for i in keyin:
    key.append(i)

k = int(input())

whole_ans = []
for i in range(k):
    ans = []
    for j in range(n):
        x = input()

        if   x == '#OOO':
            ans.append('A') 
        elif x == 'O#OO':
            ans.append('B') 
        elif x == 'OO#O':
            ans.append('C')
        elif x == 'OOO#':
            ans.append('D')
        elif x == 'OOOO':
            ans.append(' ')
        else:
            ans.append('X')
            
    whole_ans.append(ans)
    

# print('key',key)
# print('whole_ans',whole_ans)


for i in whole_ans:
    dorost = 0
    ghalat = 0
    nomre = 0
    for j in range(n):
        if i[j] == key[j]:
            dorost += 1
        if i[j] != key[j]:
            if i[j] == ' ':
                pass
            else:
                ghalat +=1
    nomre = (dorost*3) - ghalat
    print(nomre)

        
        


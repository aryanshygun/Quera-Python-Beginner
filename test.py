En = {1: 'One', 2: 'Two' , 3: 'Three', 4: 'Four'  , 5: 'Five' }
Fr  = {1: 'Un' , 2: 'Deux', 3: 'Trois', 4: 'Quatre', 5: 'Cinq'}
x = input()

xlist = list()
while x != 'End':
    a, b = x.split()
    a = int(a)
    if b == 'En':
        xlist.append(En.get(a))
    if b == 'Fr':
        xlist.append(Fr.get(a))
    x = input()

for i in xlist:
    print(i)

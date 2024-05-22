# https://quera.org/college/12547/chapter/46830/lesson/168508/?comments_page=1&comments_filter=ALL&submissions_page=1
import math

def joz(n):
    if n > 0:
        return int(n)
    elif n == 0:
        return 0
    elif n < 0:
        return int(n) - 1
    
def tabe1(n, u):
    m = n - joz(n)
    if abs(m - u) <=  0.2:
        return 1

def tabe2(n, u):
    m = n**2 + n
    if abs(m - u) <=  0.2:
       return 2
  
def tabe3(n, u):
    m = abs(-(n**3) + 1) + n**3
    if abs(m - u) <=  0.2:
        return 3


n = int(input())
xlist = []
for i in range(n):
    x, y = map(float, input().split())
    xlist.append((x, y))

ydict = {}
for r in range(len(xlist)):
    i, j = xlist[r]
    ylist = []
    ylist.append(tabe1(i, j))
    ylist.append(tabe2(i, j))
    ylist.append(tabe3(i, j))
    ydict[r + 1] = ylist

result1 = all(1 in lst for lst in ydict.values())
result2 = all(2 in lst for lst in ydict.values())
result3 = all(3 in lst for lst in ydict.values())

results = []
if result1 == True:
    results.append(1)
if result2 == True:
    results.append(2)
if result3 == True:
    results.append(3)
if result1 == False and result2 == False and result3 == False:
    print('No ones')

for i in results:
    print(i)
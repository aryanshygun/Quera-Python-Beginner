# https://quera.org/college/12547/chapter/46830/lesson/168523/?comments_page=1&comments_filter=ALL

# s = input()
# p = input()

# s = 'bb??x???'
# p = 'aab'

# l = 0
# r = len(p)

# while r <= len(s):
#     x = s[l:r]
#     print(x)

#     if x.count('a') > p.count('a') or x.count('b') > p.count('b'):
#         print('nah')
#         l += 1
#         r += 1  
#     else:
#         if x.count('b') == p.count('b') and x.count('?') == p.cou
#         print('else')
#         l += 1
#         r += 1 
#     print()

a = 'bb?'
b = 'aab'
c = ''.join(i for i in a if i not in b)
print(c)
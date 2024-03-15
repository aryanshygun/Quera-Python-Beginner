# https://quera.org/problemset/66859

import numpy as np


# import numpy 

number, base = map(int, input().split())

# number=100 # decimal
ternary=np.base_repr(number,base)
print(ternary)
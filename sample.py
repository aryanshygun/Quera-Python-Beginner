import re


def validate_num(x):
    x = str(x)
    template1 = r'^(09)\d{9}$'
    template2 = r'^(+989)\d{9}'
    template3 = r'^(00989)\d{9}'
    # print('type x', type(x))
    # if len(x) == 11:
    #     if x[0:2] == '09':
    #         if re.match(template1, x):
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False
    if re.match(template1, x):
        return True
    else:
        return False
    
print(validate_num())
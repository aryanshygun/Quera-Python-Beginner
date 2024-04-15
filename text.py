class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function


def test1():
    return 1/0

def test2():
    'wef' + 232


    
def transform_exceptions(func_ls):
    new_func_ls = []  # Create a new list to store modified elements
    for func in func_ls:
        try:
            func()
            new_func_ls.append(ExceptionProxy('ok!', func))
        except Exception as e:
            new_func_ls.append(ExceptionProxy(str(e), func))
    return new_func_ls

xlist = transform_exceptions([test1, test2])

for j in xlist:
    print('a')
    print(j.msg)
    print('b')
    print(j.function.__name__)
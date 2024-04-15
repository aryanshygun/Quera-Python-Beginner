class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function


a = ExceptionProxy('fuck', 'me')
print(a.msg)
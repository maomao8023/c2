#-*- encoding=UTF-8 -*-

def log(level, *args, **kvargs):
    def inner(func):
        def wrapper(*args, **kvargs):
            print level, 'before calling', func.__name__
            print level, 'args: ', args, 'kvargs: ', kvargs
            func(*args, **kvargs)
            print level, 'end calling ', func.__name__
        return wrapper
    return inner

@log(level = 'INFO')# 等级人为设置 可以设置多个等级
def hello(name, age):
    print 'hello', name, age

if __name__ == '__main__':
    hello(name = 'maomao', age = 2)
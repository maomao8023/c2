# -*- encoding=UTF-8 -*-

def log(level,*args, **kvargs):
    def inner(func):
        def wrapper(*args, **kvargs):
            print level, 'before calling', func.__name__
            print 'agrs: ', args, 'kvargs: ', kvargs
            func(*args, **kvargs)
            print level, 'end calling', func.__name__
        return wrapper
    return inner


@log(level = 'INFO')
def hello(name, age):
    print 'hello', name, age

if __name__ == '__main__':
    hello(name = 'maomao',age = 2) # log(hello())









'''
def shout(word="yes"):
    return word.capitalize() + "!"


print shout()
# outputs : 'Yes!'
# 输出 : 'Yes!'

# As an object, you can assign the function to a variable like any
# other object
# 如果函数是个对象，那么它就可以赋值给变量

scream = shout

# Notice we don't use parentheses: we are not calling the function, we are
# putting the function "shout" into the variable "scream".
# It means you can then call "shout" from "scream":
# 注意这里并没有使用括号，也就是说没有调用这个函数
# 我们只是让变量 "scream" 等于函数 "shout"
# 意思就是你通过调用 "scream" 函数来调用 "shout" 函数:

print scream()
# outputs : 'Yes!'

# More than that, it means you can remove the old name 'shout', and
# the function will still be accessible from 'scream'
# 另外，这还表示你可以删除老的函数名 'shout'
# 这个函数依然存在，并且可以通过 'scream' 调用

del shout
try:
    print shout()
except NameError, e:
    print e
    # outputs: "name 'shout' is not defined"

print scream()
# outputs: 'Yes!'
'''
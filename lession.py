#-*- encoding=UTF-8 -*-

'''print 1, max(2, 1),  min(5,3)
print len('xxxx'),  len([1,2,3])       #字符串的长度 数组的长度
print 3,abs(-2)                       #fabs, Math.fabs
print 4,range(1, 10, 3)
'''

class Student(object):
    '''
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def PrintAll(self):
        print 1, self.__name, self.__score
    def getName(self):
        return self.__name
    def getScore(self):
        return self.__score
    def setName(self,name):
        self.__name = name
    def setScore(self,score):
        self.__score = score
    '''
    def run(self):
        print 'student is running...'

class Maomao(Student):
    def run(self):
        print 'maomao is running quickly'

class Gougou(Student):
    def run(self):
        print 'gougou is running...'

class Bigpig(Student):
    def run(self):
        print 'bigpig is running slowly...'

def runtwice(Student):
    Student.run()
    Student.run()


if __name__ == '__main__':
    runtwice(Gougou())
    print 262 + 64 + 814 + 100
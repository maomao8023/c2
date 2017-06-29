import re
def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    p2 = re.compile('\d')
    print 1, p1.findall(str)
    print 2, p2.findall(str)
    str = 'a@163.com;b@gmail.com;c@qq.com;e@163.com;z@qq.com'
    p3 = re.compile('[\w]+@163\.com')
    print 3, p3.findall(str)
    p4 = re.compile('[\w]+@[163|qq]+\.com')
    print 4, p4.findall(str)
    str = '<html><h>title</h><body>xxx</body></html>'
    p5 = re.compile('<h>[^<]</h>')
    p6 = re.compile('<h>([^<]+)</h>')
    print 5, p5.findall(str)
    print 6, p6.findall(str)
    p7 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print 7, p7.findall(str)


    str = 'xx2016-06-11yy'
    p8 = re.compile('\d\d\d\d-\d\d-\d\d')
    print 8, p8.findall(str)
    p9 = re.compile('\d{4}-\d{2}-\d{2}')
    print 9, p9.findall(str)

if __name__ == '__main__':
    demo_re()
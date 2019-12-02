# -*- coding: utf-8 -*-

print("HelloWorld python")
print("中文")

for i in range(2, 5):
    print('i = ' + str(i))
    for j in range(i, 4):
        print('j = ' + str(j))
    else:
        print('else i = ' + str(i))
else:
    print('else finish')



def do_test():
    def do_globe():
        global str
        str = "global"
    
    # global str
    str = 'str test'
    do_globe()
    print('afer do_globe: ' + str)



str = 'str init'
do_test()
print('main: ' + str)

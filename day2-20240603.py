#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#本节内容来自廖雪峰Python基础-字符串与编码
#https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896

'''
8bit=1 byte
1 byte 能表示的最大整数位255(二进制11111111=十进制255)
在计算机内存中,统一使用Unicode编码,当需要保存到硬盘或者需要传输的时候,就转换为UTF-8编码。
用记事本编辑的时候,从文件读取的UTF-8字符被转换为Unicode字符到内存里,编辑完成后,保存的时候再把Unicode转换为UTF-8保存到文件

浏览网页的时候,服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器.所以你看到很多网页的源码上会有类似<meta charset="UTF-8" />的信息,表示该网页正是用的UTF-8编码。

'''
#在Python3中，字符串是以Unicode编码的
print('包含中文的str')
#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示, 相反，chr()是把编码转换成对应的字符
print(ord("A"))
print(chr(65))
#如果知道字符的整数编码,还可以用十六进制这么写str
print('\u4e2d\u6587')

print('ABC'.encode('ascii'))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))
#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
'''
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
'''
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print('Age: %s. Gender: %s' % (25, True))
#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('growth rate: %d %%' % 7)
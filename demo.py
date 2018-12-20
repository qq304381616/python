#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行表示可执行文件，winodws忽略
#第二行 表示读取使用utf-8解码

# hello . 包括IO
name = input('please inter your name : ')
100+200
print('hello,', name)

# 演示缩进
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

# 转义字符
print('\n\'\\')

# r'' 后面的内容不转义
print(r'\\\aa\\')

# 数值
print(2.31)
print(0xff00)
print(22e5)
print(22e-5)

# 布尔值
print(True)
print(False)
print(3>2)

print(True or False)
print(True and False)
print(not False)

print(None)

# 变量
a = 123;
print(a)

# 常量
PI = 3.14

# 除法 / 返回浮点数。 //返回整数
print('10/3 =', 10/3)
print('10//3 =', 10//3)

# 编码
print('中国')
print('A 转换为对应的整数:', ord('A'))
print('整数65转换为对应的字符: ' , chr(65))
print(r'\u4e2d\u6587 转换 ：', '\u4e2d\u6587')
print(b'ABC')
print('ABC'.encode('ascii'))
print('中国'.encode('utf-8'))

# 解码
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 忽略错误
print(b'\xe4\xb8\xad\xe6\x92'.decode('utf-8', errors='ignore'))

print(len('ABC'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# 格式化字符串 %d %f %s %x %%
print('Hello, %s' %'world')
print('Hello, %s, you have $%d' %('Michael', 100000))
print('%2d-%02d' %(3,1))
print('%.2f' % 3.1415926)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# 集合 list
names = ['name1', 'name2', 'name3']
print(names)
print(names[0])
print(names[-1])
print(len(names))
names.append('name4')
print(names)

# 集合 tuple. 和list相比，一旦初始化 不能修改。一个元素后要加,和括号区分
names = ('name1', 'name2')
print(names)
namess = ('a', 'b', ['A', 'B']) # 这种可变

# if elif else 

# 引入第三方插件，需要提前安装 python install
import aiohttp
print(aiohttp.__version__)

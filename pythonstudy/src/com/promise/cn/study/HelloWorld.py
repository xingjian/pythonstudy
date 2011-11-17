#-*- encoding: utf-8 -*-
'''
Created on 2011-11-16
@author: promise
'''
#!输出语句print
print('hello world!');
print(2 ** 10);
print(2 + 120);
print('我是中国人！');
#!变量赋值
name = 'this is first python programe!';
print(name);
print('%s is %s test %d' % ('this', 'my', 99));
#写文件
sqlfile = open('C:\\360Downloads\\menusql.txt', 'a');
print('this test abceeffff', file=sqlfile);
sqlfile.close();
#程序输入
user = input('enter login name:')
print('you login user %s' % (user))
age = input('your age:')
print('your age: %d' % (int(age) * 2))
print(age * 2)
#列表和元组
a = ['a', 'b', 'c', 'd'];
print(a)
print(a[:3])
a[1] = 2
print(a[:3]) 
b = {'1':'2', '3':'4'};
print(b)
b['5'] = '6'
print(b)
print(b.keys())
print(b['5'])
for key in b:
    print(key + b[key])

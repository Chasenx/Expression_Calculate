# -*- coding:utf-8 -*-
from sympy import diff 
from quadEquation import trans

# 微分求解的预处理
def diffpreprocess(str0):
    str0 = str0.replace(" ",'')
    if '=' in str0:
        str1 = str0.split('=')   #此时str1是一个具有两个元素的list
        str2 = str1[1]           #此时str2是一个字符串
        if str2[0] == 'd':
            str2 = str2[2:]
        if str2[-1] == ')':
            str2 = str2[:-1]
    return str2


def latex2diff(str0):
    str0 = diffpreprocess(str0)
    str0 = trans(str0)
    result = diff(str0)
    result = str(result)
    afterprocess = diffprocess(result)
    return afterprocess

# 这个函数将diff函数的输出结果转化为比较容易读的结果
def diffprocess(str0):
    str1 = str0.replace("**","^")
    str1 = str1.replace(r'(\d)(x)',"")
    str1 = str1.replace(" ","")
    return str1

if __name__ == '__main__':
    teststr = 'd y = d ( 2 6 x ^ { 2 } + 3 )'
    teststr1 = latex2diff(teststr)
    # teststr1 = diff('(x+1)/x')
    print(teststr1)



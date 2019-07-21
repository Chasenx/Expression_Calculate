# -*- coding:utf-8 -*-
from sympy import diff 
from quadEquation import trans
log = print

# 微分求解的预处理(old)
# def diffpreprocess(str0):
#     str0 = str0.replace(" ",'')  #去空格
#     if '=' in str0:
#         str1 = str0.split('=')   #此时str1是一个具有两个元素的list
#         str2 = str1[1]           #此时str2是一个字符串
#         if str2[0] == 'd':
#             str2 = str2[2:]
#         if str2[-1] == ')':
#             str2 = str2[:-1]
#     return str2

# new
def diffpreprocess(str0):
    repldict = {" ":'', "\sin":'sin', "\cos":'cos', "\ln":'ln', "\\arccos":'arccos', 
        "\\arcsin":'arcsin', "\\arctan":'arctan', "\\tan":'tan', "\sqrt":'sqrt', '\pi':'pi'}
    for k, v in repldict.items():
        str0 = str0.replace(k, v)

    # str0 = str0.replace(" ",'')  #去空格
    # str0 = str0.replace("\sin", 'sin')
    # str0 = str0.replace("\cos", 'cos')
    # str0 = str0.replace("\ln", 'ln')
    # str0 = str0.replace("\x07rccos", 'arccos')
    # str0 = str0.replace("\x07rcsin", 'arcsin')
    # str0 = str0.replace("\x07rctan", 'arctan')
    # str0 = str0.replace("\x09an", 'tan')
    # str0 = str0.replace("\sqrt", 'sqrt')

    strlist = str0.split('\\\\')

    str0 = strlist[0]
    strlist = str0.split('=')
    str0 = strlist[1]

    return str0


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
    # str1 = str1.replace(r'(\d)(x)',"")
    str1 = str1.replace(" ","")
    str1 = str1.replace("xp", "^")
    return str1

if __name__ == '__main__':
    teststr = r"y = x ( x - 1 ) ( x - 2 ) ( x - 3 ) \\ y ' ="
    print(latex2diff(teststr))


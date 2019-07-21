# -*- coding:utf-8 -*-
from sympy import solve
from quadEquation import trans
log = print

# 求解一元二次方程
def equation_Order2(str0):
    str0 = trans(str0)
    s = solve(str0)
    return s

# 求解方程组
def equation_cluster(str0):
    str0 = str0.replace(' ', '')
    str0 = str0.replace('\\begin{cases}', '')
    str0 = str0.replace('\\end{cases}', '')
    strlist = str0.split('\\\\')

    strlist = [trans(a) for a in strlist]
    # strlist = [a.replace('\x0c', 'f') for a in strlist]

    s = solve(strlist)
    return s

if __name__ == '__main__':
    test = r""
    # print(test)
    print(equation_cluster(test))


# 输入   '3 x ( x + 2 ) = 5 ( x + 2 )'
# 输出   '3*x*(x+2)-(5*(x+2))'

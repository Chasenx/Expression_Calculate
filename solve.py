# -*- coding:utf-8 -*-
import re

#求解一元一次方程的主函数
def solve(eq, var='x'):
    eq = re.sub(r'([\d\.]+)([xy])', r'\1*\2', eq)
    try:
        c = eval(eq.replace("=", "-(" ) + ")", {var: 1j})
        x = -c.real/c.imag
    except Exception as err:
        print(err)
        return
    return x

#一元一次方程转化函数，将空格去掉，乘号加上，同时自变量转化为x
def equationTrans(equa) :
    newEqua = ""
    equa = equa.replace(" ", "")
    symbol = ['+','-','*','/','=','.','(',')']
    for i in range(len(equa)):
        if (equa[i] >= '0' and equa[i] <= '9') or equa[i] in symbol:
            newEqua += equa[i]
        elif i == 0 or equa[i-1] == '*':
            newEqua += "x"
        else:
            newEqua += "*x"
    return newEqua


if __name__ == '__main__':
    eq = '2*x+10=10x+4.2 + (3x-3)/2'
    print(eq)
    eq = equationTrans(eq)
    print(eq)
    x = solve(eq)
    print('x=%s' % x)

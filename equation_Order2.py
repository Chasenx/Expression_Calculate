# -*- coding:utf-8 -*-
from sympy import solve
from quadEquation import trans

# 求解一元二次方程
def equation_Order2(str0):
    str0 = trans(str0)
    s = solve(str0)
    return s

if __name__ == '__main__':
    expr = '\frac { 2 7 x - 1 } { 1 4 } = 1 5 x + 6'
    print(expr)
    print(equation_Order2(expr))

# 输入   '3 x ( x + 2 ) = 5 ( x + 2 )'
# 输出   '3*x*(x+2)-(5*(x+2))'

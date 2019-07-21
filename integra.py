# -*- coding:utf-8 -*-
from quadEquation import trans, pairindex
from sympy import integrate
from quadEquation import pairindex
from sympy import Symbol, evaluate
log = print

# 计算不定积分
def integra1(str0):
    str0 = str0.replace(" ", "").replace('\\int', '').replace('dx', '(1)')
    str0 = trans(str0)
    result = integrate(str0)
    result = str(result)
    result = result.replace('**', '^')
    return result

# 计算定积分
def integra2(str0):
    # input: \int _ { 0 } ^ { \frac { \pi } { 2 } } \sin ( 4 x ) d x
    upstr = ''
    downstr = ''
    str0 = str0.replace(" ", "").replace('\int', '').replace('dx', '(1)')
    index1 = 1
    index2 = pairindex('{', index1, str0)
    index3 = index2 + 2
    index4 = pairindex('{', index3, str0)

    upstr = str0[index1 + 1:index2]
    downstr = str0[index3 + 1:index4]

    str0 = str0[index4 + 1:]

    str0 = trans(str0)
    upstr = trans(upstr)
    downstr = trans(downstr)

    x = Symbol('x')
    result = integrate(str0, (x, upstr, downstr))
    result1 = str(result)
    if 'x' in result1:
        result = result1.replace('**', '^')
    else:
        result = result.evalf()
    return result


if __name__ == "__main__":
    test = '\int _ { x ^ { 2 } } ^ { x ^ { 3 } } \cos ( x ) d x'
    print(integra2(test))
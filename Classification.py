# -*- coding:utf-8 -*-
from expression import calculate
from diff import latex2diff
from equation_Order2 import equation_Order2
from equation_tree import drawEquationTree

def classification(str0):
    if '=' in str0:
        str0 = str0.replace(" ",'')
        if 'dy' in str0:
            print('微分的结果是：')
            print(latex2diff(str0))
        else:
            print('方程的解是：')
            print(equation_Order2(str0))

    else:
        print('表达式的结果是：')
        print(calculate(str0))

    drawEquationTree(str0)


if __name__ == '__main__':
    teststr = '\frac { 2 x + 1 } { 4 } - 1 = x - \frac { 1 0 x + 1 } { 1 2 }'
    classification(teststr)

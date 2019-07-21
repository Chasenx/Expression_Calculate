# -*- coding:utf-8 -*-
from expression import calculate, calculate1
from diff import latex2diff
from integra import integra1,integra2
from equation_Order2 import equation_Order2
from equation_Order2 import equation_cluster
from equation_tree import drawEquationTree

def classification(str0):
    try:
        if '=' in str0:
            str0 = str0.replace(" ",'')
            if "y'" in str0:
                print('微分的结果是：')
                cal = latex2diff(str0)
                print(cal)
                return cal
            else:
                if 'cases' in str0:
                    print('方程组的解是：')
                    cal = equation_cluster(str0)
                    print(cal)
                    return cal
                else:
                    print('方程的解是：')
                    cal = equation_Order2(str0)
                    print(cal)

        elif 'int' in str0:
            str0 = str0.replace(" ",'')
            if 'int_' in str0:
                print('定积分的结果是：')
                cal = integra2(str0)
                print(cal)
            else:
                print('不定积分的结果是：')
                cal = integra1(str0)
                print(cal)   
        else:
            print('表达式的结果是：')
            cal = calculate1(str0)
            # cal = calculate(str0)  # 此函数为自己写的计算，上面那个是调库的
            print(cal) 

        # drawEquationTree(str0)    # 画树的时候使用的函数
        return cal
    except BaseException:
        return "error"

if __name__ == '__main__':
    teststr = r"\int ( 1 - \frac { 1 } { x ^ { 2 } } ) d x"
    a = classification(teststr)
    print('输出返回值是: ', a)
    

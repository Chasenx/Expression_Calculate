# -*- coding:utf-8 -*-
import re
# def solve(eq,var='x'):
#     eq1 = eq.replace("=","-(")+")"
#     c = eval(eq1,{var:1j})
#     return -c.real/c.imag

# x = solve("x-2*x+5*x-46*(235-24)=x+2")
# print(x)


def solve(eq, var='x'):
    eq = re.sub(r'([\d\.]+)([xy])', r'\1*\2', eq)
    try:
        c = eval(eq.replace("=", "-(" ) + ")", {var: 1j})
        x = -c.real/c.imag
    except Exception as err:
        print(err)
        return
    return x

if __name__ == '__main__':
    eq = '2*p+10=10p+4.2'
    print(eq)
    x = solve(eq,var='p')
    print('a=%s' % x)

# 输出：2*x+10=10x+4.2
# 输入：2a + 10 = 10*a + 4.2
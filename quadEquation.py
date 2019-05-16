# -*- coding:utf-8 -*-
import re

# 写一个函数(一元二次方程预处理)：

# 输入：'a^{2} + 2a = 3'
# 输出：'x**2+2*x-3'

# 要求：'^{2}'替换成'**2',
#     不能有空格，
#     其他子没有全部转化成x
#     '2x'这样的东西补充乘号

# 小提示：'='替换成'-(',最后补充一个')'


#二元一次方程的预处理函数
def trans(equa):
    equa = equa.replace(" ","")
    equa = re.sub("\x0crac{(.*?)}{(.*?)}", replMod, equa)
    nEqua = ''
    symbol = ['+','-','*','/','=','(',')']
    for i in range(len(equa)):
        if equa[i] >= 'a' and equa[i] <= 'z':
            if i == 0 or equa[i-1] in symbol:
                nEqua += 'x'
            else:
                nEqua += '*x'
        else:
            nEqua += equa[i]
    nEqua = nEqua.replace("^{2}", "**2")
    nEqua = re.sub("=(.*)", replEquel, nEqua)
    return nEqua

def replEquel(matched):
    newVal = "-(" + matched.group(1) + ")"
    return newVal

def replMod(matched):
    newVal = "(" + matched.group(1) + ")" + "/" + "(" + matched.group(2) + ")"
    return newVal

if __name__ == '__main__':
    expr = '- x ^ { 2 } - 6 x = - 1 0'
    print(expr)
    print(trans(expr))


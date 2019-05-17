# -*- coding:utf-8 -*-

import re
def trans(equa):
    equa = equa.replace(" ","").replace("\times", "*").replace("\div", "/").replace("^{2}", "**2")
    equa = re.sub("\x0crac{(.*?)}{(.*?)}", replMod, equa)
    nEqua = ''
    symbol = ['+','-','*','/','=']
    for i in range(len(equa)):
        if equa[i] >= 'a' and equa[i] <= 'z':
            if i == 0 or equa[i-1] in symbol:
                nEqua += 'x'
            else:
                nEqua += '*x'
        else:
            nEqua += equa[i]
    nEqua = re.sub("=(.*)", replEquel, nEqua)
    nEqua = re.sub("[1-9x](\(.*?\))", replPare, nEqua)
    return nEqua

def replEquel(matched):
    newVal = "-(" + matched.group(1) + ")"
    return newVal

def replMod(matched):
    newVal = "((" + matched.group(1) + ")" + "/" + "(" + matched.group(2) + "))"
    return newVal

def replPare(matched):
    newVal = "*" + matched.group(1)
    return newVal

if __name__ == '__main__':
    expr = "\frac { x + 1 } { x } "
    print(expr)
    print(trans(expr))


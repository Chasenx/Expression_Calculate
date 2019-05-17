import re
def trans(equa):
    equa = equa.replace(" ","").replace("\times", "*").replace("\div", "/")
    equa = re.sub("\^{([0-9]*?)}", replIndex, equa)
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
    nEqua = re.sub("=(.*)", replEquel, nEqua)
    nEqua = re.sub("[1-9x](\(.*?\))", replPare, nEqua)
    return nEqua

def replEquel(matched):
    newVal = "-(" + matched.group(1) + ")"
    return newVal

def replIndex(matched):
    newVal = "**" + matched.group(1)
    return newVal

def replMod(matched):
    newVal = "((" + matched.group(1) + ")" + "/" + "(" + matched.group(2) + "))"
    return newVal

def replPare(matched):
    newVal = "*" + matched.group(1)
    return newVal

if __name__ == '__main__':
    expr = "\frac { 1 7 x + 4 } { 7 x ^ { 10 } }"
    print(trans(expr))

# def trans(equa, flag=0):
#     flag=0 的时候 x^{数字} 转化为 x**数字
#     flag=1 的时候 x^{数字} 转化为 x^数字


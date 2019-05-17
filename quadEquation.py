import re
def trans(equa, flag=0):
    equa = equa.replace(" ","").replace("\times", "*").replace("\div", "/")
    if flag == 0:
        equa = re.sub("\^{([0-9]*?)}", replIndex0, equa)
    else :
        equa = re.sub("\^{([0-9]*?)}", replIndex1, equa)
    
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

def replIndex0(matched):
    newVal = "**" + matched.group(1)
    return newVal

def replIndex1(matched):
    newVal = "^" + matched.group(1)
    return newVal


def replMod(matched):
    newVal = "((" + matched.group(1) + ")" + "/" + "(" + matched.group(2) + "))"
    return newVal

def replPare(matched):
    newVal = "*" + matched.group(1)
    return newVal

if __name__ == '__main__':
    expr = "\frac { 1 7 x + 4 } { 7 x ^ { 3 } }"
    print(trans(expr,1))


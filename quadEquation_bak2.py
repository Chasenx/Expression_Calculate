import re
def trans(equa):
    equa = equa.replace(" ","").replace("\times", "*").replace("\div", "/")
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
    nEqua = nEqua.replace("^{2}", "**2")
    # nEqua = nEqua.replace("^{3}", "**3")
    # nEqua = nEqua.replace("^{4}", "**4")
    # nEqua = nEqua.replace("^{5}", "**5")
    # nEqua = nEqua.replace("^{6}", "**6")
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
    expr = "\frac { 1 7 x + 4 } { 7 x ^ { 2 } } "
    print(expr)
    print(trans(expr))


import re
from stack import Stack
from kmp import kmp_search
log = print

def trans(equa, flag=0):
    equa = equa.replace(" ","").replace("\\times", "*").replace("\\div", "/").replace("\\infty", 'oo')
    
    # 处理 sqrt函数
    sqrtlist = [m.start() for m in re.finditer('sqrt{', equa)]
    for n in sqrtlist:
        end = pairindex('{', n + 4, equa)
        equa = equa[:n+4] + "(" + equa[n + 5:end] + ")" + equa[end + 1:]

    # 增加把 'e^{}' 换成 'exp()'
    # equa = re.sub("e\^{(.*)}", replIndex3, equa)
    explist = [m.start() for m in re.finditer('e', equa)]
    explist.append(len(equa))
    firststr = equa[:explist[0]]
    strlist = [firststr]

    for i in range(len(explist) - 1):
        n = explist[i]
        nnext = explist[i + 1]
        # newstr = equa[n:nnext]
        if equa[n + 1:n + 3] == '^{':
            end = pairindex('{', n + 2, equa)
            # equa = equa[:n] + "exp(" + equa[n + 3:end] + ")" + equa[end + 1:]
            strlist.append("exp(" + equa[n + 3:end] + ")" + equa[end + 1:nnext])
        else:
            # equa = equa[:n] + "exp(1)" + equa[n + 1:]
            strlist.append("exp(1)" + equa[n + 1:nnext])
    equa = "".join(strlist)



    funclist = ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'ln', 'sqrt', 'pi', 'lg', 'log']
    for f in funclist:
        equa = kwprocess(f, equa)


    if flag == 0:
        equa = re.sub("\^{([0-9a-z\+\-\*\/]*)}", replIndex0, equa)
    else:
        equa = re.sub("\^{([0-9a-z\+\-\*\/]*)}", replIndex1, equa)
   
    # equa = re.sub("\\\\frac{(.*?)}{(.*?)}", replMod, equa)
    equa = fracprocess(equa)


    nEqua = ''
    symbol = ['+','-','*','/','=','(',')']
    
    for i in range(len(equa)):
        if equa[i] >= 'a' and equa[i] <= 'z':
            if i == 0 or equa[i-1] in symbol:
                nEqua += equa[i]
            else:
                nEqua += '*' + equa[i]     # 修改了不要把字母都替换成 x 这个步骤，直接原来的字母
        else:
            nEqua += equa[i]
    
    nEqua = re.sub("=(.*)", replEquel, nEqua)
    nEqua = re.sub("([1-9|x])(\(.*?\))", replPare, nEqua)
 
    # 增加把 ')x' 换成 ')*x'
    nEqua = re.sub("(\))(\w)", replIndex2, nEqua)

    repldict = {'e*x*p':'exp', ')(':')*(', 's*i*n':'sin', 'c*o*s':'cos', 'l*n':'ln',
    'a*r*c*':'arc', 't*a*n':'tan', 's*q*r*t':'sqrt', 'p*i':'pi', 'o*o':'oo', 'l*g':'lg', 'l*o*g':'log'}

    for k, v in repldict.items():
        nEqua = nEqua.replace(k, v)
   
    return nEqua


def kwprocess(key, str0):

    klen = len(key)

    str0 = str0.replace('\\' + key, key)
    # str0 = str0.replace('\x07', '\x61')
    # str0 = str0.replace('\x09', '\x74')

    str0 = str0.replace(' ', '')
    numlist = [m.start() for m in re.finditer(key, str0)]

    for n in numlist:
        if str0[n + klen:n + klen + 2] == '^{':
            index1 = n + klen
            index2 = pairindex('{', n + klen + 1, str0)
            index3 = index2 + 1
            index4 = pairindex('(', index3, str0)
            str0 = str0[:index1] + str0[index3:index4 + 1] + str0[index1:index2 + 1] + str0[index4 + 1:]
    return str0


# 括号匹配函数，找出与当前括号匹配的另外一半
def pairindex(key, index, str0):
    sta = Stack()
    dictlist = {'(':')', '[':']', '{':'}'}
    sta.push(key)
    while not sta.is_empty():
        index = index + 1
        if str0[index] in dictlist:
            sta.push(str0[index])
        if str0[index] == dictlist[sta.peek()]:
            sta.pop()
    return index


def replEquel(matched):
    newVal = "-(" + matched.group(1) + ")"
    return newVal

def replIndex0(matched):

    newVal = "**" + matched.group(1)
    return newVal

def replIndex1(matched):
    newVal = "^" + matched.group(1)
    return newVal

def replIndex2(matched):
    newVal = ")*" + matched.group(2)
    return newVal

def replIndex3(matched):
    newVal = "exp(" + matched.group(1) + ")"
    return newVal

def replMod(matched):
    newVal = "((" + matched.group(1) + ")" + "/" + "(" + matched.group(2) + "))"
    return newVal

def replPare(matched):
    newVal = matched.group(1) + "*" + matched.group(2)
    return newVal

def logprocess():
    pass

def fracprocess(str0):
    # fraclist = [m.start() for m in re.finditer('\frac', str0)]
    fraclist = kmp_search(str0, '\\frac')

    fraclist.append(len(str0))

    while len(fraclist) != 1:
        firststr = str0[:fraclist[0]]
        strlist = [firststr]

        index1 = n + 5
        index2 = pairindex('{', index1, str0)
        index3 = index2 + 1
        index4 = pairindex('{', index3, str0)

        strlist.append(str0[:n] + "((" + str0[index1 + 1:index2] + ")/(" + str0[index3 + 1:index4] + "))" + str0[index4 + 1:strlist[-1]])
        fraclist = kmp_search(str0, '\\frac')
        fraclist.append(len(str0))




    # for i in range(len(fraclist) - 1):
    #     n = fraclist[i]
    #     nnext = fraclist[i + 1]
        
    #     index1 = n + 5
    #     index2 = pairindex('{', index1, str0)
    #     index3 = index2 + 1
    #     index4 = pairindex('{', index3, str0)
        
    #     strlist.append("((" + str0[index1 + 1:index2] + ")/(" + str0[index3 + 1:index4] + "))" + str0[index4 + 1:nnext])

    # result = "".join(strlist)
    return result




if __name__ == '__main__':
    expr = "e ^ { 3 x } - \frac { e } { x }"
    test = r"\frac { \frac{5}{4} } { 4 } \lg ( 2 5 ) + 2 ^ { \sin( 3 ) } + \lg ( 2 \sqrt { 2 } )"
    print(trans(test))

# -*- coding:utf-8 -*-
import re

class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[-1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 压栈
    def push(self, item):
        self.items.append(item)

    # 出栈
    def pop(self):
        return self.items.pop()

def priority(element):
    numbers = {
        ')':0,
        '+':1,
        '-':1,
        '*':2,
        '/':2,
        '(':3
    }
    return numbers.get(element,None)

#计算后缀表达式的函数，输入一个后缀表达式的list
def postfixExpression(postlist):
    mystack = Stack()
    for tempstr in postlist:
        if (tempstr == '+' or tempstr == '-' or tempstr == '*' or tempstr == '/'):
            secondnum = mystack.peek()
            mystack.pop()
            firstnum = mystack.peek()
            mystack.pop()
            
            if (tempstr == '+'):
                sum = firstnum + secondnum
                mystack.push(sum)
            if (tempstr == '-'):
                sum = firstnum - secondnum
                mystack.push(sum)
            if (tempstr == '*'):
                sum = firstnum * secondnum
                mystack.push(sum)
            if (tempstr == '/'):
                sum = firstnum / secondnum
                mystack.push(sum)
        else:
            num = float(tempstr)
            mystack.push(num)

    return mystack.peek()

#中缀表达式转后缀表达式
def InfixToPostfi(strlist):
    operatorstr = ['+','-','*','/','(',')']
    PostfiOutvec = []
    operatorstack = Stack()
    for element in strlist:
        if (element in operatorstr):
            if (operatorstack.is_empty()):   #如果操作符栈空，直接入栈
                operatorstack.push(element)
            else:
                if (element == ')'):  #如果当前操作符是右括号
                    while (operatorstack.peek() != '('):
                        PostfiOutvec.append(operatorstack.peek())
                        operatorstack.pop()
                    operatorstack.pop()  #这里是删除左括号
                else:
                    curpri = priority(element)
                    while (not operatorstack.is_empty()):
                        top = operatorstack.peek()
                        toppor = priority(top)
                        if ((curpri <= toppor) and (top != '(')):
                            PostfiOutvec.append(top)
                            operatorstack.pop()
                        else:
                            break
                    operatorstack.push(element)   
        else:
            PostfiOutvec.append(element)
    while(not operatorstack.is_empty()):
        PostfiOutvec.append(operatorstack.peek())
        operatorstack.pop()
    return PostfiOutvec

#字符串转list
def str2list(str0):
    pattern = re.compile(r'[+|\-|*|/|(|)]')
    strlist = [m.start() for m in pattern.finditer(str0)]
    
    a = -1
    result = []
    for i in strlist:
        if (a != i-1):
            result.append(str0[a+1:i])
        result.append(str0[i])
        a = i
    if (a != len(str0)-1):
        result.append(str0[a+1:])

    return result

#字符串计算函数
def calculate(str0):
    str1 = str2list(str0)
    str2 = InfixToPostfi(str1)
    result = postfixExpression(str2)
    return result

# 测试代码

str0 = '3.14+(6-3.2)*(40+12)'
strtest = '17.8+3.6-((3)/(10))*((7)/(3))'

print(strtest)
print(calculate(strtest))

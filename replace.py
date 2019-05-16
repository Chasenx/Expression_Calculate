# -*- coding:utf-8 -*-

# 这个函数来把Latex表达式转化为程序可以计算的表达式
# 主要包括除号的替换，分式转化，乘号替换，去空格等
# 目前的分式转化有点问题

import re
def expressionRepl(expr) :
    expr = expr.replace(" ","")
    expr = expr.replace("\times", "*")
    expr = re.sub("\x0crac{(.*?)}{(.*?)}", repl, expr)
    return expr

def repl(matched):
    newVal = "(" + matched.group(1) + ")" + "/" + "(" + matched.group(2) + ")"
    return newVal

if __name__ == '__main__':
    expr = r"\frac { 2 5 + 6 x } { 2 4 }"
    print(expr)
    print(expressionRepl(expr))
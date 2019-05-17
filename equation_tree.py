# -*- coding:utf-8 -*-
from suffixExpr import suffixExpr2Tree,Node
from BinTreeVisualization import Latex2tree,draw
from quadEquation import trans
from diff import diffpreprocess
from suffixExpr import Node

def drawEquationTree(str0):
    flag = 0
    if '=' in str0:
        str0 = str0.replace(" ",'')
        if 'dy' in str0:
            str1 = str0.split('=')   #此时str1是一个具有两个元素的list
            str2 = str1[1]           #此时str2是一个字符串
            str3 = str2[1:]          #去掉开头的一个d
            total = trans(str3, flag=1)
            flag = 1
        else:
            str1 = str0.split('=')
            subleft = str1[0]
            subright = str1[1]

            subleft = trans(subleft, flag=1)
            subright = trans(subright, flag=1)
            total = subleft + '=' + subright
    else:
        total = trans(str0, flag=1)
           
    # total = total.replace("**",'^')  #这两句话以后可以不要
    root = Latex2tree(total)

    if flag:
        first = Node("\'")
        dNode = Node('d')
        first.right = root
        first.left = dNode
        root = first
    draw(root)

    

if __name__ == '__main__':
    teststr = '\frac { 1 5 - x } { 4 } - \frac { 1 4 + x } { 2 } = 0'
    drawEquationTree(teststr)


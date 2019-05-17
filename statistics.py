# -*- coding:utf-8 -*-

def statistics(expr):
    dic = {}
    for i in range(len(expr)):
        if expr[i] in dic:
            temp = expr[i]
            for j in range(dic[expr[i]]):
                expr[i] += " "
            dic[temp] += 1
        else:
            dic[expr[i]] = 1
    return expr

if __name__ == '__main__':
    expr = ['3.4', '3.4', '+', '+', '3.4','3.4']
    print(statistics(expr))
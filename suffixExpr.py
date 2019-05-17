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

class Node(object):
    def __init__(self, v='') :
        self.left = None
        self.right = None
        self.val = v


def suffixExpr2Tree(expr):
    stack = Stack()
    # symbol = ['+','-','*','/']
    root = None
    for i in expr:
        if re.match(r'^[\+|\-|\*|/|=|\^]',i):
            cur = Node(i)
            right = stack.pop()
            if isinstance(right, Node):
                cur.right = right
            else:
                cur.right = Node(right)
            left = stack.pop()
            if isinstance(left, Node):
                cur.left = left
            else:
                cur.left = Node(left)
            stack.push(cur)
            root = cur
        else:
            stack.push(i)
    return root

if __name__ == '__main__':
    expr = ['3.4', '2', '4.6', '3', '-', '^', '+', '4', '2.3', '-', '+']
    root = suffixExpr2Tree(expr)
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.left.right.right.right.val)
    print(root.left.right.val)
    print(root.right.val)
    print(root.left.left.val)
    print(root.right.right.val)

    if re.match(r'^[\+|\-|\*|/]','/     '):
        print('yes')
    

# -*- coding:utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
from expression import str2list,InfixToPostfi
from quadEquation import trans
from suffixExpr import suffixExpr2Tree
from statistics import statistics

def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.val] = (x, y)
    if node.left:
        G.add_edge(node.val, node.left.val)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.val, node.right.val)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)

def draw(node):   # 以某个节点为根画图
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 8))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=300, node_color='w', font_size=15)
    plt.show()

def Latex2tree(str0):
    str1 = str2list(str0)
    # print(str1)
    str2 = InfixToPostfi(str1)
    # print(str2)
    str3 = statistics(str2)
    # print(str3)
    tree = suffixExpr2Tree(str3)
    return tree

if __name__ == '__main__':
    str0 = '4 x'
    # strtest = '17.8+3.6-(3/10)*(7+3) -14'
    print(str0)
    str0 = trans(str0)
    str1 = str2list(str0)
    # print(str1)

    str2 = InfixToPostfi(str1)
    # print(str2)

    str3 = statistics(str2)
    # print(str3)

    root = suffixExpr2Tree(str3)

    draw(root)

# -*- coding:utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
from expression import *

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
    fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    plt.show()

if __name__ == '__main__':
    str0 = '3.14+(6-3.2)*(40/6)'
    strtest = '17.8+3.6-(3/10)*(7+3) -14'
    str1 = str2list(str0)
    str2 = InfixToPostfi(str1)
    root = suffixExpr2Tree(str2)

    print(strtest)
    print(calculate(str0))
    # print(root.right.left.left.val)
    # print(root.right.left.right.val)
    # print(root.right.right.left.val)
    # print(root.right.right.right.val)

    draw(root)

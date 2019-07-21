from pylatexenc.latex2text import LatexNodes2Text
from quadEquation import trans
from sympy import diff
import re
log = print


    # input: \log _ { 3 } ( \frac { \sqrt [ 4 ] { 2 7 } } { 3 } ) + \lg ( 2 5 )


def kwprocess(key, str0):
  
    str0 = str0.replace('\\' + key, key)
    str0 = str0.replace(' ', '')

    numlist = [m.start() for m in re.finditer(key, str0)]

    for n in numlist:
        if str0[n + 3] == '^' and str0[n + 4] == '{':
            index1 = n + 3
            i = index1
            while str0[i] != '}':
                i = i + 1
            index2 = i
            index3 = i + 1
            while str0[i] != ')':
                i = i + 1
            index4 = i
            str0 = str0[:index1] + str0[index3:index4 + 1] + str0[index1:index2 + 1] + str0[index4 + 1:]
    return str0


if __name__ == "__main__":
    key = 'cos'
    str0 = "\cos ^ { 2 } ( x ) - \cos ^{8} ( x ^ { 2 } )"
    print(kwprocess(key, str0))


def equationTrans(equa) :
    newEqua = ""
    equa = equa.replace(" ", "")
    symbol = ['+','-','*','/','=','.']
    for i in range(len(equa)):
        if (equa[i] >= '0' and equa[i] <= '9') or equa[i] in symbol:
            newEqua += equa[i]
        elif i == 0 or equa[i-1] == '*':
            newEqua += "x"
        else:
            newEqua += "*x"
    return newEqua

if __name__ == '__main__':
    expr = "2a + 10 = 10*a + 4.2"
    print(expr.replace(" ", ""))
    print(equationTrans(expr))

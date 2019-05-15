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
    expr = r"\frac { 2 5 + 6 x } { 2 4 } = 4 x"
    print(expr)
    print(expressionRepl(expr))
def prefixToInfix(prefix):
    stack = []
     
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            stack.append(prefix[i])
            i -= 1
        else:
           
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(conver):
    if conver == "*" or conver == "+" or conver == "-" or conver == "/" or conver == "^" or conver == "(" or conver == ")":
        return True
    else:
        return False
 
if __name__=="__main__":
    str = input("Type String to convert prefix to Infix : ").upper()
    print("Prefix to Infix covertion is : ",prefixToInfix(str))
     

def isOperator(opr):
 
    if opr == "+":
        return True
 
    if opr == "-":
        return True
 
    if opr == "/":
        return True
 
    if opr == "*":
        return True
 
    return False
 
 
 
def postToPre(post_exp):
 
    string1 = []
 
    length = len(post_exp)
 
    for i in range(length):
 
        if (isOperator(post_exp[i])):
 
            op1 = string1[-1]
            string1.pop()
            op2 = string1[-1]
            string1.pop()
 
            temp = post_exp[i] + op2 + op1
 
            string1.append(temp)
 
        else:
 
            string1.append(post_exp[i])
 
    
    ans = ""
    for i in string1:
        ans += i
    return ans
 
if __name__ == "__main__":
 
    post_exp = input("Type String to convert postfix to prefix expression: ").upper()
     
    print("Prefix : ", postToPre(post_exp))
 
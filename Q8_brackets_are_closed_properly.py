
def areBracketsBalanced(expr):
    stack = []
 
    for char in expr:
        if char in ["(", "{", "["]:
 
            stack.append(char)
        else:
 
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    if stack:
        return False
    return True
 
if __name__ == "__main__":

    expr = input("Type brakets to check all the brackets are closed properly: ")
 
    if areBracketsBalanced(expr):
        print("All the brackets are closed correctly")
    else:
        print("All the brackets are not closed correctly")
 

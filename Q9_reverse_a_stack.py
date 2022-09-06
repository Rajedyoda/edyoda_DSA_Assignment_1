class StackNode:
     
    def __init__(self, data):
         
        self.data = data
        self.next = None
 
class Stack:
     
    def __init__(self):
          
        self.top = None
      
    def push(self, data):
     
        if (self.top == None):
            self.top = StackNode(data)
            return
         
        stack1 = StackNode(data)
        stack1.next = self.top
        self.top = stack1
      
    def pop(self):
     
        stack1 = self.top
        self.top = self.top.next
        return stack1
  
    def display(self):
     
        stack1 = self.top
         
        while (stack1 != None):
            print(stack1.data, end = ' ')
            stack1 = stack1.next
         
    def reverse(self):
 
        prev = self.top
        cur = self.top
        cur = cur.next
        succ = None
        prev.next = None
         
        while (cur != None):
            succ = cur.next
            cur.next = prev
            prev = cur
            cur = succ
         
        self.top = prev
     
if __name__=='__main__':
     
    stack1 = Stack()
    stack1.push(int(input("Type Stack integer to push 1st element: ")))
    stack1.push(int(input("Type Stack integer to push 2nd element: ")))
    stack1.push(int(input("Type Stack integer to push 3rd element: ")))
    stack1.push(int(input("Type Stack integer to push 4th element: ")))
     
    print("Original Stack:")
    stack1.display()
    print()
      
    stack1.reverse()
  
    print("Reversed Stack:")
    stack1.display()
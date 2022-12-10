#without import single linked list
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None

class stack():
    def __init__(self):
        self.head = None
        self.SizeOfStack = 0
    '''
        Removes first element from the beginning of the linked list.
        pops the top and returns the removed element.
    '''    
    def pop(self):
        if self.isempty():
            return "Error"
        popped = self.head
        self.head = self.head.next
        popped.next = None
        self.SizeOfStack =self.SizeOfStack- 1
        return popped.data
    '''
    Return the top of the stack
    '''    
    def peek(self):
        if self.isempty():
            return "Error"
        top = self.head
        return top.data
    '''
    Push the element at the beginning of the linked list which
    means on the top of our stack.
    '''
    def push(self,element):

        new_node = Node(element)
        new_node.next = None
        if self.head is None:
            self.head = new_node
            self.SizeOfStack =self.SizeOfStack+1
            return
        new_node.next = self.head
        self.head = new_node
        self.SizeOfStack =self.SizeOfStack+1

    
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def Size(self):
        return self.SizeOfStack
    
    def printList(self, node):
        print("[",end="")
        while(node is not None and node.next is not None):
            print(node.data,end=', ')
            node = node.next
        if(node is not None):
            print(node.data,end="")
        print("]")

global operand ,operator
operand = ['a','b','c']
operator = ['-','+','*','/','^']

class IExpressionEvaluator(stack):
    def __init__(self):
        self.piority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3,'(':-1}
        self.postfix = ""
        stack.__init__(self)
    
    def infixToPostfix(self,expression):
        global operand ,operator

        if expression[-1] in operator:
                return "Error"
        if expression[0] == '/' or expression[0] == '*' or expression[0] == '^':
                return "Error"
        
        for i in range(len(expression)):

            if expression[i] in operand:
                self.postfix += expression[i]
            
            elif expression[i] == "(" :
                if expression[i+1] == ")":
                    return "Error"
                self.push(expression[i])
            
            elif expression[i] == ")" :
                while (not self.isempty()) and self.peek() !='(':
                    self.postfix += self.pop()
                if (not self.isempty()) and self.peek() =='(':
                    self.pop()
                else:
                    return "Error"

            elif expression[i] in operator and expression[i+1] in operator:
                return 'Error'

            elif  self.isempty() :
                if i == 0 and expression[i] =='+':
                    pass
                else:
                    self.push(expression[i])
            elif expression[i]=='-' and (expression[i+1] in operator[1:]):
                return "Error"
            else:
                try:
                    while not self.isempty() and self.piority[expression[i]] <= self.piority[self.peek()]:
                        self.postfix += self.pop()
                except:
                    return 'Error'
                self.push(expression[i])    
        
        while not self.isempty():
            if self.peek() == '(':
                return "Error"
            self.postfix += self.pop()
        
        return self.postfix


    def get_value(self,op):
        global a,b,c
        if  op =='a':
            return a
        elif  op =='b':
            return b
        elif  op =='c':
            return c


    def evaluate(self,expression):
        for i in expression:
            if i in operand:
                self.push(self.get_value(i))
            else:
                x = self.pop()
                if not self.isempty():
                    y = self.pop()
                    if i == '+':
                        self.push(x+y)
                    elif i == '-':
                        self.push(y-x)
                    elif i == '*':
                        self.push(y*x)
                    elif i == '^':
                        self.push(y**x)
                    elif i =='/':
                        try:
                            self.push(int(y/x))
                        except:
                            return "Error"
                else:
                    self.push(-1*x)
        return int(self.peek())            



if __name__=='__main__':
    global a,b,c
    try:
        Eva = IExpressionEvaluator()
        infix_ex = input().replace("^--","^").replace("/--","/").replace("+-- ", "+")  .replace("*--","*").replace("---","-").replace("+- ", "-").replace("--","+")
        
        a = int(input()[2:])
        b = int(input()[2:])
        c = int(input()[2:])

        try:
            infix_ex.remove('')
        except:
            pass
        if len(infix_ex) <=0:
            print("Error")
        else:
            
            postfix_ex = Eva.infixToPostfix(infix_ex)
            print(postfix_ex)    
            if postfix_ex != "Error":
                result = Eva.evaluate(postfix_ex)
                print(result)
    except:
        print("Error")
        
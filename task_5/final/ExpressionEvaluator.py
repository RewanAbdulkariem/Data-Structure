from stackImplementation import *

global operand ,operator
operand = ['a','b','c']
operator = ['-','+','*','/','^']
#inherit stack class to use its method in this class
'''
This class to convert infix expression to postfix expression 
and then send the postfix expression to function evaluate to 
evaluate its value
'''
class IExpressionEvaluator(stack):
    def __init__(self):
        self.piority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3,'(':-1}      # indicate the piority of each operation as power operator has the most piority for example
        self.postfix = ""                                                   # string to store the expression of the postfix
        stack.__init__(self)                                                #inherit stack class
    '''
    infixToPostfix function used to convert infix expression
    to postfix expression through some steps :
    First: we check the vality of the expression if not valid
    exit the fuction and return Error not valid expression as
    1-start with operator */^ or end with */+-^ 
    2-empty () or have open or close braket only 
    3- operator followed by operator 
    Second : If operand ,Store in postfix. 
            If open braket ,Push in stack. 
            If close braket ,pop and store in postfix 
                expression until reach the open braket
            If no thing from above so it's operator 
            so if stack empty then push it to stack
            If not empty and piorty of the operator lower than 
            or equal the poirty of the top of the stack
            then pop from the stack and store it in postfix expression
            until one of the two coditions failed then push this operator
            in the stack
    third : After that if the stack still not empty ,pop from it and 
            store in the expression post fix 
    '''
    def infixToPostfix(self,expression):
        global operand ,operator

        if expression[-1] in operator:
                return "Error"
        if expression[0] in operator[2:]:
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

            elif expression[i] in operator[2:] and expression[i+1] in operator[2:]:
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

    '''
    only get the value of the operand 
    '''
    def get_value(self,op):
        global a,b,c
        if  op =='a':
            return a
        elif  op =='b':
            return b
        elif  op =='c':
            return c

    '''
    Evalute the value of the expression by compensating thier value
    in the expression push in the stack until you reach operator 
    pop the last two operand and evalute the operation then push the result
    in the stack and so on  
    '''
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
                        self.push(round(y**x))
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
        infix_ex = input().replace("^--","^").replace("/--","/").replace("+-- ", "+")  .replace("*--","*").replace("---","-").replace("+- ", "-")
        for i in range(len(infix_ex)):
            if infix_ex[:2] == "--":
                infix_ex = infix_ex[2:]
            else:
                infix_ex = infix_ex.replace("--",'+')
        
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
        
        
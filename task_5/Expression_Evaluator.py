from stackImplementation import *
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
                if self.isempty():
                        return "Error"
                while (not self.isempty()) and self.peek() !='(':
                    self.postfix += self.pop()
                    if (not self.isempty()) and self.peek() =='(':
                        self.pop()
                        break
                    elif self.isempty():
                        return "Error"
            elif expression[i] in operator and expression[i+1] in operator:
                return 'Error'

            elif self.isempty() :
                if i == 0 and expression[i] =='+':
                    pass
                elif i == 0:
                    print("Error")
                else:
                    self.push(expression[i])
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
        if not infix_ex:
            print("Error")
        else:
            
            postfix_ex = Eva.infixToPostfix(infix_ex)
            print(postfix_ex)            
            result = Eva.evaluate(postfix_ex)
            print(result)
    except:
        print("Error")
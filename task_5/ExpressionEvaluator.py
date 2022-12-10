from stackImplementation import *
global operand ,operator
operand = ['a','b','c']
operator = ['-','+','*','/','^']

class IExpressionEvaluator(stack):
    def __init__(self):
        self.piority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3,'(':-1}
        self.postfix = ""
        stack.__init__(self)
    
    def infixToPostfix(self,exp):
        global operand ,operator
        if len(exp)<= 2:
            return "Error"
        if exp[0] in operator[2:]:
            return "Error"
        if exp[-1] in operator:
            return "Error"

        for i in range(len(exp)):
            if exp[i] in operand:
                try:
                    if exp[i+1] in operand:
                        return "Error"
                except:
                    pass
                self.postfix += exp[i]
            
            elif exp[i] == "(":
                try:
                    if exp[i+1] == ")":
                        return "Error"
                except:
                    pass
                self.push(exp[i])

            elif exp[i] == ")":
                if self.isempty():
                        return "Error"
                while (not self.isempty()) and self.peek() !='(':
                    self.postfix += self.pop()
                    if (not self.isempty()) and self.peek() =='(':
                        self.pop()
                        break
                    elif self.isempty():
                        return "Error"
           
            elif self.isempty() :
                if i == 0 and exp[i] == '+':
                    pass
                else:
                    self.push(exp[i])

            else:
                try:
                    while not self.isempty() and self.piority[exp[i]] <= self.piority[self.peek()]:
                        self.postfix += self.pop()
                except:
                    return 'Error'
                self.push(exp[i])   

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

        postfix_ex = Eva.infixToPostfix(infix_ex)
        print(postfix_ex)            
        result = Eva.evaluate(postfix_ex)
        print(result)
    except:
        print("Error")

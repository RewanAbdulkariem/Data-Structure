import math

global a,b,c
a = 0
b = 0
c = 0
class Evaluator() :
    # calculate the piority of operators:
    def  Pr( ch) :
        x = -1
        if (ch=='+'):
            x = 1
        elif(ch=='-'):
            x = 1
        elif(ch=='*'):
            x = 2
        elif(ch=='/'):
            x = 2
        elif(ch=='^'):
            x = 3
        elif(ch=='('):
            x = -1
        else:
            print("Error")   
        return x
    # convert infix expression to postfix:
    def  infixToPostfix(self, expression) :
        res =  ""
        stack =  []
        i = 0
        i = 0
        while (i < len(expression)) :
            ch = expression[i]
            # refuse the expression which start with operator
            if (expression[0] == '+' or expression[0] == '*' or expression[0] == '/' or expression[0] == '^') :
                print("Error")
                
            # refuse the expression which end with operator
            if (expression[len(expression) - 1] == '+' or expression[len(expression) - 1] == '*' or expression[len(expression) - 1] == '/' or expression[len(expression) - 1] == '^' or expression[len(expression) - 1] == '-') :
                print("Error")
                
            # if the turn on operand put it in result
            if (ch == 'a' or ch == 'b' or ch == 'c') :
                res = res + str(ch)
            elif(ch == '(') :
                if (expression[i + 1] == ')') :
                    print("Error")
                    
                stack.append(ch)
            elif(ch == ')') :
                while (not (len(stack) == 0) and stack[-1] != ord('(')) :
                    res = res + str(stack.pop())
                if (not (len(stack) == 0) and stack[-1] == ord('(')) :
                    stack.pop()
                else :
                    print("Error")
                    
            elif((len(stack) == 0)) :
                stack.append(ch)
            elif(not (len(stack) == 0) and ch == '-' and expression[i - 1] == '-') :
                if (i == 1) :
                    stack.pop()
                elif(expression[i - 2] == 'a' or expression[i - 2] == 'b' or expression[i - 2] == 'c') :
                    stack.pop()
                    stack.append('+')
            elif(ch == '-' and (expression[i + 1] == '+' or expression[i + 1] == '/' or expression[i + 1] == '*' or expression[i + 1] == '^')) :
                print("Error")
                
            else :
                while (not (len(stack) == 0) and Evaluator.Pr(ch) <= Evaluator.Pr(stack[-1])) :
                    res = res + str(stack.pop())
                stack.append(ch)
            i += 1
        # if there is '('  without ')' print error
        while (not (len(stack) == 0)) :
            if (stack[-1] == ord('(')) :
                print("Error", end ="")
                
            res += stack.pop()
        return res
    # get the value if the input operand
    def  getval(self, m) :
        global a,b,c
        e = 0
        if (m=='a'):
            e = a
        elif(m=='b'):
            e = b
        elif(m=='c'):
            e = c
        else:
            print("Error")
            
        return e
    @staticmethod
    def  operand( c) :
        if (ord(c) >= 97 and ord(c) <= 99) :
            return True
        else :
            return False
    # evaluate the expression after being converted to postifix
    def  evaluate(self, expression) :
        Fstack =  []
        j = 0
        while (j < len(expression)) :
            h = expression[j]
            if (Evaluator.operand(h)) :
                Fstack.append(self.getval(h))
            else :
                # take operand 1 from the stack
                x = Fstack.pop()
                if (not (len(Fstack) == 0)) :
                    # take operand 2 from the stack
                    y = Fstack.pop()
                    # check operator
                    if (expression[j]=='+'):
                        Fstack.append((x + y))
                    elif(expression[j]=='-'):
                        Fstack.append((y - x))
                    elif(expression[j]=='*'):
                        Fstack.append((x * y))
                    elif(expression[j]=='^'):
                        Fstack.append(int(math.pow(y,x)))
                    elif(expression[j]=='/'):
                        try :
                            s = int((int(y / x)))
                        except :
                            print("Error")
                            
                        Fstack.append(int((int(y / x))))
                else :
                    Fstack.append(-1 * x)
            j += 1
        # return the top value in the stack
        return int(Fstack[-1])
    class Node :
        data = 0
        link = None
        def __init__(self, d) :
            self.link = None
            self.data = d
        def __init__(self, d,  n) :
            self.data = d
            self.link = n
        def setLink(self, n) :
            self.link = n
        def setData(self, d) :
            self.data = d
        def  getLink(self) :
            return self.link
        def  getData(self) :
            return self.data
    top = None
    size = 0
    tail = None
    def linkedStack(self) :
        self.top = None
        Evaluator.size = 0
    #  Function to check if stack is empty
    def  isEmpty(self) :
        return (self.top == None)
    # Function to get the size of the stack
    def  size(self) :
        return Evaluator.size
    # Function to push an element to the stack
    def push(self, data) :
        nptr = Node(data, None)
        if (self.top == None) :
            self.top = nptr
        else :
            nptr.setLink(self.top)
            self.top = nptr
        Evaluator.size += 1
    # Function to pop an element from the stack
    def  pop(self) :
        if (self.isEmpty()) :
            raise Exception("Error")
        ptr = self.top
        self.top = ptr.getLink()
        Evaluator.size -= 1
        return ptr.getData()
    #  Function to check the top element of the stack
    def  peek(self) :
        if (self.isEmpty()) :
            raise Exception("Error")
        return self.top.getData()
    def main( args) :
        global a,b,c
        r = Evaluator()
        # take the expression and replace all the repeated followed operator
        try :
            infix = input()
            infix = infix.replace("^--","^").replace("/--","/").replace("+-- ","+").replace("*--","*").replace("---","-").replace("+- ","-")
            # take value of operand
            a = int(input()[2:])
            b = int(input()[2:])
            c = int(input()[2:])
            result = r.infixToPostfix(infix)
            print(result)
            y = int(r.evaluate(result))
            print(y)
        except :
            print("Error")
    

if __name__=="__main__":
    Evaluator.main([])
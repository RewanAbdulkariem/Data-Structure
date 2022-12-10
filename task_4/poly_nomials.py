from single_linkedlist import*
class polynomialSolver:
    def __init__(self):
        self.polA = SingleLinkedlist()
        self.polB = SingleLinkedlist()
        self.polC = SingleLinkedlist()
        self.polR = SingleLinkedlist()
    
    def setPolynomialSolver(self,poly,terms):
        if poly == 'A':
            for i in range(len(terms)):
                self.polA.add(terms[i][0])
        elif poly == 'B':
            for i in range(len(terms)):
                self.polB.add(terms[i][0])
        elif poly == 'C':
            for i in range(len(terms)):
                self.polC.add(terms[i][0])
        else:
            print(poly+"Error")

    def printlist(self,poly):
        if poly == 'A':
            print(self.polA.size())
            return self.getPolynomial(self.polA)
        elif poly == 'B':
            return self.getPolynomial(self.polB)
        elif poly == 'C':
            return self.getPolynomial(self.polC)
        elif(poly=='R'):
            return self.getPolynomial(self.polR)
        else:
            print("")
    
    def getPolynomial(self,poly):
        polyrepresentation =""   
        print(poly.size())

        for i in range(poly.size()):
                exp = poly.size() - 1 - i
                no = poly.get(i)
                num = poly.get(i+1)
                if no != 0:
                    if exp == 0:
                        polyrepresentation += str(no)
                    elif exp == 1:
                        if no ==1:
                            polyrepresentation += "x"
                        else:
                            polyrepresentation += str(no) + "x"
                else:
                    if no == 1:
                        polyrepresentation += "x^" + str(exp)
                    else:
                        polyrepresentation += str(no) + "x^" + str(exp)
                if i != poly.size() -1 and num >0:
                    polyrepresentation +="+"
        return polyrepresentation

    def clearPolynomial(self,poly):
        if poly == 'A':
            self.polA.clear()
        elif poly == 'B':
            self.polB.clear()
        elif poly == 'C':
            self.polC.clear()
        else:
            print("Error")

    def evaluatePolynomial(self,poly,value):
        if poly == 'A':
            return self.evaluate(self.polA, value)
        elif poly == 'B':
            return self.evaluate(self.polB, value)
        elif poly == 'C':
            return self.evaluate(self.polC, value)
        else:
            print("Error")

    def evaluate (self,poly,value):
        result = 0
        for i in range(poly.size()):
            p = int(poly.get(i))
            result += p * value^(poly.size()-1-i)
        return result

    def add(self,poly1,poly2):
        operand1= self.getOperand(poly1)
        operand2= self.getOperand(poly2)
        self.polR.clear()
        self.polR = self.addition(operand1,operand2)

        return self.LinkedlistToArray(self.polR)

    def getOperand(self,poly):
        if poly == 'A':
            return self.polA
        elif poly == 'B':
            return self.polB
        elif poly == 'C':
            return self.polC
        else:
            print("Error")
    
    def addition(self,poly1,poly2):
        polyadd = SingleLinkedlist()
        self.appendzeros(poly1,poly2)

        for i in range(poly1.size):
            additionresult = int(poly1.get(i))+int(poly2.get(i))
            polyadd.add(additionresult)

        return polyadd

    def subtract(self,poly1,poly2):
        operand1= self.getOperand(poly1)
        operand2= self.getOperand(poly2)
        self.polR.clear()
        self.polR = self.subtraction(operand1,operand2)

        return self.LinkedlistToArray(self.polR)

    def subtraction(self,poly1,poly2):
        polysub = SingleLinkedlist()
        self.appendzeros(poly1,poly2)

        for i in range(poly1.size):
            additionresult = int(poly1.get(i)) - int(poly2.get(i))
            polysub.add(additionresult)

        return polysub

    def multiply(self,poly1,poly2):
        operand1= self.getOperand(poly1)
        operand2= self.getOperand(poly2)
        self.polR.clear()
        self.polR = self.multiplication(operand1,operand2)

        return self.LinkedlistToArray(self.polR)
    
    def multiplication(self,poly1,poly2):
        polymul = SingleLinkedlist()
        multsize = poly1.size() + poly2.size() - 1

        for i in range(multsize):
            polymul.add(0)
            
        for i in range(poly1.size()):
            exp1 = poly1.size()-1-i
            for j in range(poly2.size()):
                exp2 = poly2.size() - 1 - j
                mult_exp = exp1 + exp2
                mult_index = multsize -1 - mult_exp
                mult_result = mult_result +int(polymul.get(mult_index))
                polymul.set(mult_index,mult_result)
    
        return polymul
    
    def appendZeroes(self,poly1,poly2):
        differ = poly1.size()-poly2.size()

        if differ > 0:
            for i in range(abs(differ)):
                poly2.addToIndex(0,0)
        else:
            for i in range(abs(differ)):
                poly1.addToIndex(0,0)
    
    def LinkedlistToArray(self,poly):
        ls=[]
        for i in range(poly.size()):
            ls[i][0] = int(poly.get(i))
            ls[i][1] = poly.size()-1-i
        return ls



if __name__=='__main__':
    polynomial = polynomialSolver()
    exitt=False
    while not exitt:
        op = input()
        if op =="set":
            poly = input()
            coffi = input()[1:-1].split(",")
            n = len(coffi)
            ls = [[],[]]
            c = []
            e = []
            
            if len(coffi)==1 and coffi[0].isEmpty():
                print("Error")
            else:
                for i in range (n):
                    c.append(int(coffi[i]))
                    e.append(n-1-i)

                ls[0].append(c)
                ls[1].append(e)

            
            polynomial.setPolynomialSolver(poly, ls)
            
        elif op =="print":
            polynomial.printlist(input())
        elif op =="add":
            var1 = input()
            var2 = input()
            polynomial.add(var1, var2)
        elif op =="sub":
            var1 = input()
            var2 = input()
            polynomial.subtract(var1, var2)

        elif op == "mult":
            var1 = input()
            var2 = input()
            polynomial.multiply(var1, var2)

        elif op == "clear":
            var = input()
            polynomial.clearPolynomial(var)

        elif op =="eval":
            var = input()
            value = int(input())  

            polynomial.evaluatePolynomial(var, value);
        else:
            print("Error")
            exitt = True


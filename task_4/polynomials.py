class Node:
	def __init__(self,coeff,exp):
		self.coeff = coeff
		self.exp = exp
		self.next = None
    
def setPolynomialSolver(poly,terms):
    pass

def printlist(poly):
    pass

def clearPolynomial(poly):
    pass

def evaluatePolynomial(poly,value):
    pass

def add(poly1,poly2):
    pass

def subtract(poly1,poly2):
    pass

def multiply(poly1,poly2):
    pass


if __name__=='__main__':
    while True:
        op = input()
        if op =="set":
            poly = input()
            coffi = input()[1:-1].split(",")
            setPolynomialSolver(poly,coffi)

        elif op =="print":
            printlist(input())
        elif op =="add":
            var1 = input()
            var2 = input()
        elif op =="sub":
            var1 = input()
            var2 = input()
        elif op == "mult":
            var1 = input()
            var2 = input()
        elif op == "clear":
            var = input()
        elif op =="eval":
            var = input()
            value = int(input())    


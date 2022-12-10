class node:
    def __init__(self, coeff = 0, pow = 0, nxt = None):
        self.coefficient = coeff
        self.power = pow
        self.next = nxt

global A,B,C,R
R = node()
A = node()
B = node()
C = node()

def setPolynomialSolver(poly , terms):
   ls = []
   n =len(terms) -1
   for i in range(len(terms)):
      ls.append([terms[i],n-i])
   if(poly == "A" ):
      create_poly(A,ls)
   elif (poly == "B"):
      create_poly(B,ls)
   elif (poly == "C"):
      C = create_poly(C,ls)

def create_poly(poly,ls):
   for e in ls:
      new_node = node(e[0],e[1])
      new_node.next = None
      if poly == None:
            poly = new_node
      else:
            temp = poly
            while temp.next != None:
               temp = temp.next
            temp.next = new_node
   return poly 

def printlist(poly):
   if poly == 'A':
      show_poly(A)
   elif poly == 'B':
      show_poly(B)
   elif poly == 'C':
      show_poly(C)
   elif(poly=='R'):
      show_poly(R)
   else:
      print(" Error")

def show_poly(head):
   temp = head
   while temp.next != None:
      print(str(temp.coefficient) + 'x^' + str(temp.power), end = ' + ')
      temp = temp.next
      if temp.next == None:
            print(str(temp.coefficient) + 'x^' + str(temp.power))

def clearPolynomial(poly):
   if poly == 'A':
      clear(A)
   elif poly == 'B':
      clear(B)
   elif poly == 'C':
      clear(C)
   elif poly == 'R':
      clear(R)

def clear(poly):
   while (head != None):
      head = head.next
   return head

def evaluatePolynomial(poly,value):
   pass

def add(poly1,poly2):
   result = node()
   prev = result
   while poly1 and poly2:
      if poly1.power > poly2.power:
            prev.next = poly1
            prev = poly1
            poly1 = poly1.next
      
      elif poly1.power < poly2.power:
            prev.next = poly2
            prev = poly2
            poly2 = poly2.next

      else:
            coef = poly1.coefficient + poly2.coefficient
      if coef: 
            prev.next  = poly1
            
            poly1 = poly1.next
            poly2 = poly2.next
   if (poly1 != None):
      prev.next = poly1

   if (poly2 != None):
      prev.next = poly2
   return result.next    


while True:
    op = input()
    if op =="set":
        print("set:")
        poly = input()
        coffi = input()[1:-1].split(",")
        setPolynomialSolver(poly,coffi)
    elif op =="print":
        print("print :")
        printlist(input())
    else:
        print("Error")
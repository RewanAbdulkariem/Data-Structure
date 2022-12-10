#class to create node and each node consists of power and coefficient and has a pointer to next node
class node:
    def __init__(self, coeff = 0, pow = 0, nxt = None):
        self.coefficient = int(coeff)
        self.power = int(pow)
        self.next = nxt


global A,B,C,R
R = node()
A = node()
B = node()
C = node()
global exit
exit = False
"""
In this function, first we create a 2D list first 
row represent coeffient and the second represent 
power .then, we check which variable to store our 
polynomial in ,then directed to function named 
create_poly
"""
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
      create_poly(C,ls)
"""
this function create the single linked list of 
polynomial
"""
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
"""
printlist fuction first check the variable
head stored in then call the function 
show_poly to print the polynomial by it's 
usual form
"""
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
    i=0
    if temp == None:
        print([])
        return
    while(temp.next != None):
         temp = temp.next
         if  ( temp.coefficient >0) and  (i>0):
            print("+",end="")
         
         if temp.power ==1:
            if (temp.coefficient == 1) :
               print('x',end="")
            elif (temp.coefficient == -1) :
                  print('-x',end="")
            elif (temp.coefficient !=0 ) :
               print(f'{temp.coefficient}x',end="")
         elif (temp.coefficient == 1) :
            print(f'x^{temp.power}',end="")
         elif (temp.coefficient == -1) :
                print(f'-x^{temp.power}',end="")
         elif (temp.coefficient !=0 ) and (temp.power ==0) :
            print(temp.coefficient,end="")
            
         elif  temp.coefficient !=0  :
            print(f'{temp.coefficient}x^{temp.power}', end="")
         i=i+1
         if  temp.next ==None:
            print()
"""
clearPolynomial fuction first check the variable
head stored in and then call the function clear 
to clear the linked list
"""
def clearPolynomial(poly):
   if poly == 'A':
      clear(A)
   elif poly == 'B':
      clear(B)
   elif poly == 'C':
      clear(C)
   elif poly == 'R':
      clear(R)

def clear(head):
   while (head != None):
      head = head.next
   return head
"""
evaluatePolynomial fuction first check the variable
head stored in and then call the function evalute to 
solve to equation for given value
"""
def evaluatePolynomial(poly,value):
        if poly == 'A':
            return evaluate(A, value)
        elif poly == 'B':
            return evaluate(B, value)
        elif poly == 'C':
            return evaluate(C, value)
        elif poly == 'R':
            return evaluate(R, value)
        else:
            return ("Error")

def evaluate (poly,value):
   temp = poly.next
   result = 0 
   if temp == None:
      return "Error"
   else:
      while temp != None:
         result += temp.coefficient * (value**temp.power)
         temp = temp.next
      return result

def add(poly1,poly2):
   if poly1 == 'A' and poly2 =='A' :
      addition(A.next,A.next)
   elif poly1 == 'B' and poly2 =='B' :
      addition(B.next,B.next)
   elif poly1 == 'A' and poly2 =='B' :
      addition(A.next,B.next)
   elif poly1 == 'B' and poly2 =='A' :
      addition(B.next,A.next)
   else:
      print( "Error")

def addition(head1, head2):
    temp = R
    while(head1 != None or head2 != None):
        if(head1.power == head2.power):
            cof = int(head1.coefficient) + int(head2.coefficient)
            temp.next = node(cof,head1.power)
            head1 = head1.next
            head2 = head2.next

        elif(head1.power > head2.power):
            temp.next = node(head1.ccoefficient,head1.power)
            head1 = head1.next

        else:
            temp.next = node(head2.ccoefficient,head2.power)
            head2 = head2.next
        temp = temp.next
    return R.next
    
def subtract(poly1,poly2):
   if poly1 == 'A' and poly2 =='A' :
      subtraction(A.next,A.next)
   elif poly1 == 'B' and poly2 =='B' :
      subtraction(B.next,B.next)
   elif poly1 == 'A' and poly2 =='B' :
      subtraction(A.next,B.next)
   elif poly1 == 'B' and poly2 =='A' :
      subtraction(B.next,A.next)

def subtraction(head1,head2):
   temp = R
   while(head1 != None or head2 != None):
      if(head1.power == head2.power):
         cof = int(head1.coefficient) - int(head2.coefficient)
         temp.next = node(cof,head1.power)
         head1 = head1.next
         head2 = head2.next

      elif(head1.power > head2.power):
         temp.next = node(head1.ccoefficient,head1.power)
         head1 = head1.next

      else:
         temp.next = node(head2.ccoefficient,head2.power)
         head2 = head2.next
      temp = temp.next
   return R.next

def multiply(poly1,poly2):
   if poly1 == 'A' and poly2 =='A' :
      multiplication(A.next,A.next)
   elif poly1 == 'B' and poly2 =='B' :
      multiplication(B.next,B.next)
   elif poly1 == 'A' and poly2 =='B' :
      multiplication(A.next,B.next)
   elif poly1 == 'B' and poly2 =='A' :
      multiplication(B.next,A.next)

def multiplication(head1,head2):
   temp = R
   ptr1 = head1
   ptr2 = head2
   while (ptr1 != None):
      while (ptr2 != None):
         cof = ptr1.coefficient * ptr2.coefficient
         power = ptr1.power + ptr2.power
         temp.next = node(cof,power)
         ptr2 = ptr2.next
         temp = temp.next
      ptr2 =head2
      ptr1 = ptr1.next
   add_DuplicatedTerms(R.next);
   return R.next

def add_DuplicatedTerms(poly):
   temp1=poly
   temp2=None
   dup = None
   while ( temp1 != None and temp1.next != None): 
      temp2 = temp1
      while(temp2.next != None):
         if temp1.power == temp2.next.power:
            temp1.coefficient = temp1.coefficient + temp2.next.coefficient
            dup = temp2.next
            temp2.next = temp2.next.next
         else:
            temp2 = temp2.next
          
      temp1 = temp1.next




while not exit:
   try:
      op = input()
      if op =="set":
         poly = input()
         coffi = input()[1:-1].split(",")
         try:
            coffi.remove('')
         except:
            pass
         if not coffi:
            print("Error")
            exit = True
         else:
            setPolynomialSolver(poly,coffi)
      elif op =="print":
         printlist(input())
      elif op =="add":
         var1 = input()
         var2 = input()
         add(var1,var2)
         show_poly(R)
      elif op =="sub":
         var1 = input()
         var2 = input()
         subtract(var1,var2)
         show_poly(R)

      elif op == "mult":
         var1 = input()
         var2 = input()
         multiply(var1,var2)
         show_poly(R)
      elif op == "clear":
         var = input()
         show_poly(clearPolynomial(var))
      elif op =="eval":
         var = input()
         value = int(input())
         eva = evaluatePolynomial(var,value)
         if eva == "Error":
            exit = True
            print("Error") 
         else:
            print(eva) 
      else:
         print("Error")
   except EOFError:
      exit = True
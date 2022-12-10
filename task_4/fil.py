import math


class Solution :
    polynomialSolver = None
    class ILinkedList :
        # *
        #         * Inserts a specified element at the specified position in the list.
        #         * @param index
        #         * @param element
        def add(self, index,  element) :
            pass
        # *
        #         * Inserts the specified element at the end of the list.
        #         * @param element
        def add(self, element) :
            pass
        # *
        #         * @param index
        #         * @return the element at the specified position in this list.
        def  get(self, index) :
            pass
        # *
        #         * Replaces the element at the specified position in this list with the
        #         * specified element.
        #         * @param index
        #         * @param element
        def set(self, index,  element) :
            pass
        # *
        #         * Removes all of the elements from this list.
        def clear(self) :
            pass
        # *
        #         * @return true if this list contains no elements.
        def  isEmpty(self) :
            pass
        # *
        #         * Removes the element at the specified position in this list.
        #         * @param index
        def remove(self, index) :
            pass
        # *
        #         * @return the number of elements in this list.
        def  size(self) :
            pass
        # *
        #         * @param fromIndex
        #         * @param toIndex
        #         * @return a view of the portion of this list between the specified fromIndex and toIndex, inclusively.
        def  sublist(self, fromIndex,  toIndex) :
            pass
        # *
        #         * @param o
        #         * @return true if this list contains an element with the same value as the specified element.
        def  contains(self, o) :
            pass
    class DoubleLinkedList(Solution.ILinkedList) :
        class Node :
            data = 0
            next = None
            previous = None
            def __init__(self, data) :
                self.data = data
                self.next = None
                self.previous = None
            def setData(self, data) :
                self.data = data
            def  getData(self) :
                return self.data
        head = None
        tail = None
        size = 0
        def  size(self) :
            return self.size
        def add(self, element) :
            data = int(element)
            newNode = Node(data)
            if (self.head == None) :
                self.head = newNode
                self.tail = newNode
                self.size += 1
                return
            current = self.head
            while (current.next != None) :
                current = current.next
            current.next = newNode
            newNode.previous = current
            self.tail = newNode
            self.size += 1
        def add(self, index,  element) :
            if (index >= self.size or index < 0) :
                return
            data = int(element)
            if (self.head == None) :
                self.head = Node(data)
                self.size += 1
                return
            newNode = Node(data)
            if (index == 0) :
                self.head.previous = newNode
                newNode.next = self.head
                self.head = newNode
                self.size += 1
                return
            current = self.head
            i = 1
            while (i < index) :
                current = current.next
                i += 1
            newNode.next = current.next
            current.next = newNode
            newNode.previous = current
            if (newNode.next != None) :
                newNode.next.previous = newNode
            self.size += 1
        def  get(self, index) :
            if (index >= self.size or index < 0) :
                return -1
            current = self.head
            i = 0
            while (i < index) :
                current = current.next
                i += 1
            return current.getData()
        def set(self, index,  element) :
            data = int(element)
            if (index < self.size) :
                current = self.head
                i = 0
                while (i < index) :
                    current = current.next
                    i += 1
                current.setData(data)
        def  isEmpty(self) :
            return self.size == 0
        def remove(self, index) :
            current = self.head
            if (index == 0) :
                self.head = self.head.next
                self.head.previous = None
                self.size -= 1
            else :
                i = 1
                while (i < index) :
                    current = current.next
                    i += 1
                if (index == self.size - 1) :
                    current.next = None
                    self.tail = current
                else :
                    temp = current.next
                    current.next = current.next.next
                    if (current.next.next != None) :
                        current.next.next.previous = current
                    temp = None
                self.size -= 1
        def clear(self) :
            self.head = None
            self.size = 0
        def  contains(self, element) :
            data = int(element)
            current = self.head
            while (current != None) :
                if (current.getData() == data) :
                    return True
                current = current.next
            return False
        def  sublist(self, fromIndex,  toIndex) :
            doubleLinkedList = DoubleLinkedList()
            if (fromIndex >= self.size or toIndex >= self.size or fromIndex < 0 or toIndex < 0) :
                return doubleLinkedList
            current = self.head
            i = 0
            while (i < fromIndex) :
                current = current.next
                i += 1
            i = fromIndex
            while (i <= toIndex) :
                doubleLinkedList.add(current.getData())
                current = current.next
                i += 1
            return doubleLinkedList
        def printList(self) :
            if (self.head == None) :
                print("[]", end ="")
                return
            current = self.head
            print("[", end ="")
            i = 0
            while (i < self.size) :
                print(current.getData(), end ="")
                current = current.next
                if (i != self.size - 1) :
                    print(", ", end ="")
                i += 1
            print("]", end ="")
    class IPolynomialSolver :
        # *
        #     * Set polynomial terms (coefficients & exponents)
        #     *
        #     * @param poly:  name of the polynomial
        #     * @param terms: array of [coefficients][exponents]
        def setPolynomial(self, poly,  terms) :  Throws Exception
            pass
        # *
        #     * Print the polynomial in ordered human readable representation
        #     *
        #     * @param poly: name of the polynomial
        #     * @return: polynomial in the form like 27x^2+x-1
        def  print(self, poly) :
            pass
        # *
        #     * Clear the polynomial
        #     *
        #     * @param poly: name of the polynomial
        def clearPolynomial(self, poly) :  Throws Exception
            pass
        # *
        #     * Evaluate the polynomial
        #     *
        #     * @param poly:  name of the polynomial
        #     * @param value: the polynomial constant value
        #     * @return the value of the polynomial
        def  evaluatePolynomial(self, poly,  value) :  Throws Exception
            pass
        # *
        #     * Add two polynomials
        #     *
        #     * @param poly1: first polynomial
        #     * @param poly2: second polynomial
        #     * @return the result polynomial
        def  add(self, poly1,  poly2) :
            pass
        # *
        #     * Subtract two polynomials
        #     *
        #     * @param poly1: first polynomial
        #     * @param poly2: second polynomial
        #     * @return the result polynomial
        def  subtract(self, poly1,  poly2) :
            pass
        # *
        #     * Multiply two polynomials
        #     *
        #     * @param poly1: first polynomial
        #     * @param poly2: second polynomial
        #     * @return: the result polynomial
        def  multiply(self, poly1,  poly2) :
            pass
    class PolynomialSolver(Solution.IPolynomialSolver) :
        polA = None
        polB = None
        polC = None
        polR = None
        def __init__(self) :
            self.polA = DoubleLinkedList()
            self.polB = DoubleLinkedList()
            self.polC = DoubleLinkedList()
            self.polR = DoubleLinkedList()
        def setPolynomial(self, poly,  terms) :  Throws Exception
            if (poly=='A'):
                i = 0
                while (i < len(terms)) :
                    self.polA.add(terms[i][0])
                    i += 1
            elif(poly=='B'):
                i = 0
                while (i < len(terms)) :
                    self.polB.add(terms[i][0])
                    i += 1
            elif(poly=='C'):
                i = 0
                while (i < len(terms)) :
                    self.polC.add(terms[i][0])
                    i += 1
            else:
                raise Exception("Error")
        def  print(self, poly) :
            if (poly=='A'):
                return self.getPolynomial(self.polA)
            elif(poly=='B'):
                return self.getPolynomial(self.polB)
            elif(poly=='C'):
                return self.getPolynomial(self.polC)
            elif(poly=='R'):
                return self.getPolynomial(self.polR)
            else:
                return ""
        def  getPolynomial(self, polynomial) :
            polynomialRepresentation =  java.lang.StringBuilder()
            i = 0
            while (i < polynomial.size()) :
                exponent = polynomial.size() - 1 - i
                no = int(polynomial.get(i))
                Num = int(polynomial.get(i + 1))
                if (no != 0) :
                    if (exponent == 0) :
                        polynomialRepresentation.append(no)
                    elif(exponent == 1) :
                        if (no == 1) :
                            polynomialRepresentation.append("x")
                        else :
                            polynomialRepresentation.append(no).append("x")
                    elif(no == 1) :
                        polynomialRepresentation.append("x^").append(exponent)
                    else :
                        polynomialRepresentation.append(no).append("x^").append(exponent)
                    if (i != polynomial.size() - 1 and Num > 0) :
                        polynomialRepresentation.append("+")
                i += 1
            return polynomialRepresentation.toString()
        def clearPolynomial(self, poly) :  Throws Exception
            if (poly=='A'):
                self.polA.clear()
            elif(poly=='B'):
                self.polB.clear()
            elif(poly=='C'):
                self.polC.clear()
            else:
                raise Exception("Error")
        def  evaluatePolynomial(self, poly,  value) :  Throws Exception
            if (poly=='A'):
                return self.evaluate(self.polA, value)
            elif(poly=='B'):
                return self.evaluate(self.polB, value)
            elif(poly=='C'):
                return self.evaluate(self.polC, value)
            else:
                raise Exception("Error")
        def  evaluate(self, polynomial,  value) :
            result = 0
            i = 0
            while (i < polynomial.size()) :
                p = int(polynomial.get(i))
                result += p * math.pow(value,polynomial.size() - 1 - i)
                i += 1
            return result
        def  add(self, poly1,  poly2) :
            operand1 = self.getOperand(poly1)
            operand2 = self.getOperand(poly2)
            self.polR.clear()
            self.polR = self.addition(operand1, operand2)
            return self.linkedListTo2DArray(self.polR)
        def  getOperand(self, poly) :
            if (poly=='A'):
                return self.polA
            elif(poly=='B'):
                return self.polB
            elif(poly=='C'):
                return self.polC
            else:
                return DoubleLinkedList()
        def  addition(self, poly1,  poly2) :
            polyAddition = DoubleLinkedList()
            self.appendZeroes(poly1, poly2)
            i = 0
            while (i < poly1.size()) :
                addResult = int(poly1.get(i)) + int(poly2.get(i))
                polyAddition.add(addResult)
                i += 1
            return polyAddition
        def  subtract(self, poly1,  poly2) :
            operand1 = self.getOperand(poly1)
            operand2 = self.getOperand(poly2)
            self.polR.clear()
            self.polR = self.subtract(operand1, operand2)
            return self.linkedListTo2DArray(self.polR)
        def  subtract(self, poly1,  poly2) :
            polySubtact = DoubleLinkedList()
            self.appendZeroes(poly1, poly2)
            i = 0
            while (i < self.polA.size()) :
                subtractResult = int(poly1.get(i)) - int(poly2.get(i))
                polySubtact.add(subtractResult)
                i += 1
            return polySubtact
        def  multiply(self, poly1,  poly2) :
            operand1 = self.getOperand(poly1)
            operand2 = self.getOperand(poly2)
            self.polR.clear()
            self.polR = self.multiply(operand1, operand2)
            return self.linkedListTo2DArray(self.polR)
        def  multiply(self, poly1,  poly2) :
            polyMultiply = DoubleLinkedList()
            multSize = poly1.size() + poly2.size() - 1
            i = 0
            while (i < multSize) :
                polyMultiply.add(0)
                i += 1
            i = 0
            while (i < self.polA.size()) :
                exp1 = poly1.size() - 1 - i
                j = 0
                while (j < poly2.size()) :
                    exp2 = poly2.size() - 1 - j
                    multExp = exp1 + exp2
                    multIndex = multSize - 1 - multExp
                    multResult = int(poly1.get(i)) * int(poly2.get(j))
                    multResult = multResult + (int(polyMultiply.get(multIndex)))
                    polyMultiply.set(multIndex, multResult)
                    j += 1
                i += 1
            return polyMultiply
        def appendZeroes(self, poly1,  poly2) :
            diffSize = poly1.size() - poly2.size()
            if (diffSize > 0) :
                i = 0
                while (i < diffSize) :
                    poly2.add(0, 0)
                    i += 1
            elif(diffSize < 0) :
                i = 0
                while (i < abs(diffSize)) :
                    poly1.add(0, 0)
                    i += 1
        def  linkedListTo2DArray(self, polynomial) :
            R = [[0] * (2) for _ in range(20)]
            i = 0
            while (i < polynomial.size()) :
                R[i][0] = int(polynomial.get(i))
                R[i][1] = polynomial.size() - 1 - i
                i += 1
            return R
    def __init__(self) :
        self.polynomialSolver = PolynomialSolver()
    @staticmethod
    def main( args) :
        scanner =  "Python-inputs"
        solution = Solution()
        polynomialSolver = solution.polynomialSolver
        input = None
        operation = None
        poly1 = ' '
        poly2 = ' '
        exit = False
        while (scanner.hasNextLine() and not exit) :
            operation = input()
            if (operation=="set"):
                poly1 = input()[0]
                input = input().replaceAll("\\[|\\]","")
                s = input.split(",")
                arr = [[0] * (2) for _ in range(len(s))]
                try :
                    if (len(s) == 1 and s[0].isEmpty()) :
                        raise Exception("Error")
                    else :
                        i = 0
                        while (i < len(s)) :
                            arr[i][0] = int(s[i])
                            arr[i][1] = len(s) - 1 - i
                            i += 1
                except java.lang.Exception as e :
                    print(e.getMessage())
                    exit = True
                try :
                    polynomialSolver.setPolynomial(poly1, arr)
                except java.lang.Exception as e :
                    print(e.getMessage())
                    exit = True
            elif(operation=="print"):
                poly1 = input()[0]
                print(polynomialSolver.print(poly1))
            elif(operation=="add"):
                poly1 = input()[0]
                poly2 = input()[0]
                polynomialSolver.add(poly1, poly2)
                print(polynomialSolver.print('R'))
            elif(operation=="sub"):
                poly1 = input()[0]
                poly2 = input()[0]
                polynomialSolver.subtract(poly1, poly2)
                print(polynomialSolver.print('R'))
            elif(operation=="mult"):
                poly1 = input()[0]
                poly2 = input()[0]
                polynomialSolver.multiply(poly1, poly2)
                print(polynomialSolver.print('R'))
            elif(operation=="clear"):
                poly1 = input()[0]
                try :
                    polynomialSolver.clearPolynomial(poly1)
                except java.lang.Exception as e :
                    print(e.getMessage())
                    exit = True
                print("[" + polynomialSolver.print(poly1) + "]")
            elif(operation=="eval"):
                poly1 = input()[0]
                value = input()
                try :
                    polynomialSolver.evaluatePolynomial(poly1, value)
                    print(polynomialSolver.evaluatePolynomial(poly1, value))
                except java.lang.Exception as e :
                    print(e.getMessage())
                    exit = True
            else:
                print("Error")
                exit = True
        scanner.close()
    

if __name__=="__main__":
    Solution.main([])
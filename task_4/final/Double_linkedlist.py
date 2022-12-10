# A node of the doubly linked list
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
class DoublyLinkedList:
     # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
    
    def add(self,element):
        new_node = Node(element)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        temp = self.head
        while (temp.next is not None):
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        return
    
    def addToIndex(self,index ,element):
        new_node = Node(element)
        if index <0 or index >self.size():
            return 0
        elif index == 0:
            new_node = Node(element)
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            for i in range(0, index-1):
                if(temp != None):
                    temp = temp.next
            if(temp != None):
                new_node.next = temp.next
                new_node.prev = temp
                temp.next = new_node  
                if (new_node.next != None):
                    new_node.next.prev = new_node
            else:
                return
    def get(self,index):
        if index <0 or index >self.size():
            print("Error")
        temp = self.head
        for i in range(0, index):
            if(temp != None):
                temp = temp.next
        if temp !=  None:
            print (temp.data)
        else:
            print("Error")

    def set(self,index,element):
        if dll.remove(index) == 0: 
            print("Error")
        else:
            self.addToIndex(index,element)
            dll.printList(dll.head)


    def clear(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
        dll.printList(dll.head)

                
    def isEmpty(self):
        if self.head == None:
            print(True)
        else:
            print("False")


    def remove(self,index):
        
        if index < 0 or index >=self.size():
            return 0
        elif index == 0 and self.head != None:
            nodetodelete = self.head
            self.head = self.head.next
            nodetodelete = None
            if self.head != None:
                self.head.prev =None
        else:
            temp = self.head
            for i in range(0, index-1):
                if(temp != None):
                    temp = temp.next
            if (temp != None) and (temp.next != None):
                nodeToDelete = temp.next
                temp.next = temp.next.next
                if(temp.next != None):
                    temp.next.prev = temp  
                nodeToDelete = None 
            else:
                return

    def sublist(self,fromindex,toindex):
        temp = self.head
        for i in range(0, fromindex):
            if(temp != None):
                temp = temp.next
            else:
                return
        print("[",end="")
        for i in range(fromindex,toindex):
            if temp is not None and temp.next is not None:
                print(temp.data,end=', ')
                temp = temp.next
        print(temp.data,end="]")

    def size(self):
        temp = self.head
        i=0
        while(temp != None):
            temp = temp.next
            i+=1

        return i

    def contains(self, elemnt):
        found = False
        temp = self.head
        while(temp != None):
            if temp.data == elemnt:
                found= True
                break
            else:
                found = False
            temp = temp.next
        return found

    def printList(self, node):
        print("[",end="")
        while(node is not None and node.next is not None):
            print(node.data,end=', ')
            node = node.next
        if(node is not None):
            print(node.data,end="")
        print("]")

if __name__=='__main__':
    dll = DoublyLinkedList()
    ls = input()[1:-1].split(",")
    if (ls[0]):
        for i in ls:
            dll.add(int(i))
    #dll.printList(dll.head)
    op = input()

    if op == "add":
        dll.add(int(input()))
        dll.printList(dll.head)

    elif op =="addToIndex":
        index = int(input())
        element = int(input())
        if dll.addToIndex(index,element) == 0 :
            print("Error")
        else:
            dll.printList(dll.head)

    elif op =="get":
        dll.get(int(input()))

    elif op =="set":
        index = int(input())
        element = int(input())
        dll.set(index,element)
    
    elif op =="clear":
        dll.clear()
    
    elif op =="isEmpty":
        dll.isEmpty()

    elif op =="remove":
        if dll.remove(int(input())) == 0:
            print("Error")
        else:
            dll.printList(dll.head)


    elif op =="sublist":
        index1 = int(input())
        index2 = int(input())
        if (index2>=index1 and index1>=0 and index2<dll.size()):
            dll.sublist(index1,index2)
        else:
            print("Error")
    
    elif op =="contains":
        print(dll.contains(int(input())))

    elif op =="size":
        print(dll.size())
    


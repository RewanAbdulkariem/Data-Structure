# A node of the single linked list
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
 
class SingleLinkedlist:
     # Constructor for empty single Linked List
    def __init__(self):
        self.head = None
    
    def add(self,element):
        new_node = Node(element)
        new_node.next = None
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while (temp.next is not None):
            temp = temp.next
        temp.next = new_node
        return
    
    def addToIndex(self,index ,element):
        new_node = Node(element)
        if index <0 or index >self.size():
            return 0
        elif index == 0:
            new_node = Node(element)
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(0, index-1):
                if(temp != None):
                    temp = temp.next
            if(temp != None):
                new_node.next = temp.next
                temp.next = new_node  
            else:
                return
    def get(self,index):
        if index <0 or index >self.size():
            return "Error"
        temp = self.head
        for i in range(0, index):
            if(temp != None):
                temp = temp.next
        if temp !=  None:
            return temp.data
        else:
            return "Error"

    def set(self,index,element):
        if dll.remove(index) == 0: 
            return "Error"
        else:
            self.addToIndex(index,element)
            return


    def clear(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None

                
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False


    def remove(self,index):
        
        if index < 0 or index >=self.size():
            return 0
        elif index == 0 and self.head != None:
            self.head = self.head.next

        else:
            temp = self.head
            for i in range(0, index-1):
                if(temp != None):
                    temp = temp.next
            if (temp != None) and (temp.next != None):
                temp.next = temp.next.next
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
    dll = SingleLinkedlist()
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
        print(dll.get(int(input())))

    elif op =="set":
        index = int(input())
        element = int(input())
        if dll.set(index,element) == "Error":
            print("Error")
        else:
            dll.printList(dll.head)
    
    elif op =="clear":
        dll.clear()
        dll.printList(dll.head)
    
    elif op =="isEmpty":
        print(dll.isEmpty())

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
    
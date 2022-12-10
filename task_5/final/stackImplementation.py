#without import single linked list
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None

class stack():
    def __init__(self):
        self.head = None
        self.SizeOfStack = 0
    '''
        Removes first element from the beginning of the linked list.
        pops the top and returns the removed element.
    '''    
    def pop(self):
        if self.isempty():
            return "Error"
        popped = self.head
        self.head = self.head.next
        popped.next = None
        self.SizeOfStack =self.SizeOfStack- 1
        return popped.data
    '''
    Return the top of the stack
    '''    
    def peek(self):
        if self.isempty():
            return "Error"
        top = self.head
        return top.data
    '''
    Push the element at the beginning of the linked list which
    means on the top of our stack.
    '''
    def push(self,element):

        new_node = Node(element)
        new_node.next = None
        if self.head is None:
            self.head = new_node
            self.SizeOfStack =self.SizeOfStack+1
            return
        new_node.next = self.head
        self.head = new_node
        self.SizeOfStack =self.SizeOfStack+1

    '''
    check the state of the stack if empty or not
    if there is no head so stack empty
    
    '''
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
    '''
    Get the size of the stack
    '''
    def Size(self):
        return self.SizeOfStack

    def printList(self, node):
        print("[",end="")
        while(node is not None and node.next is not None):
            print(node.data,end=', ')
            node = node.next
        if(node is not None):
            print(node.data,end="")
        print("]")

if __name__=='__main__':
    ls = input()[1:-1].split(",")
    try:
        ls.remove('')
    except:
        pass
    st = stack()
    if ls:
        for i in range(len(ls)):
            st.push(int(ls[len(ls)-i-1]))

    op = input()

    if op == "push":
        st.push(int(input()))
        st.printList(st.head)

    elif op == "pop":
        if st.pop() == "Error":
            print("Error")
        else:
            st.printList(st.head)
    
    elif op == "peek":
        top = st.peek()
        if top == "Error":
            print("Error")
        else:
            print(top)

    elif op == "isEmpty":
        print(st.isempty())   

    elif op == "size":
        print(st.Size())
    else:
        print("Error")



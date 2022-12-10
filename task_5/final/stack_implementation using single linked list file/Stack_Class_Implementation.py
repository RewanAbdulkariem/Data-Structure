from single_linkedlist import *
class stack(SingleLinkedlist):
    def __init__(self,s):
        self.head = None
        self.SizeOfStack = s
    '''
        Removes first element from the beginning of the linked list.
        pops the top and returns the removed element.
    '''    
    def pop(self):
        if self.isEmpty():
            return "Error"
        popped = self.head
        self.head = self.head.next
        popped.next = None
        self.SizeOfStack =self.SizeOfStack- 1
        return popped
    '''
    Return the top of the stack
    '''    
    def peek(self):
        if self.isEmpty():
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
            return
        new_node.next = self.head
        self.head = new_node
        self.SizeOfStack =self.SizeOfStack+1

    
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def Size(self):
        print( self.SizeOfStack)

if __name__=='__main__':
    exit= False
    ls = input()[1:-1].split(",")
    try:
        ls.remove('')
    except:
        pass
    st = stack(len(ls))
    if ls:
        for i in ls:
            st.add(int(i))

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
        st.Size()
    else:
        print("Error")






            


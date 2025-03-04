class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedL:
    def __init__(self):
        self.head=None
        
    def display(self):
        # if self.head is None:
        #     print("LinkedList is Empty")
        # else:
        new_node = self.head
        while new_node:
            print(new_node.data,"-->",end=" ")
            new_node = new_node.next
                
s=LinkedL()

n = Node(10)
s.head=n

n1 = Node(20)
n.next = n1

n2 = Node(30)
n1.next = n2

n3 = Node(40)
n2.next = n3

s.display()
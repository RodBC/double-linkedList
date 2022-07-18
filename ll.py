class Node:
  def __init__(self, data):
    self.data = data 
    self.next = None 
    self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None

    def push_back(self, data): 
        new_node = Node(data)
        new_node.prev = self.tail

        if self.tail == None:  
            self.head = new_node 
            self.tail = new_node
            new_node.next = None 
                    
        else: 
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node 

    def days_to_sell(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.tail
        days = 1
        while itr:
            if itr >= itr.prev:
                days >= 1
            
 
ll = DoublyLinkedList()
ll.push_back(1)
ll.push_back(2)
ll.push_back(3)
ll.push_back(4)
ll.print()
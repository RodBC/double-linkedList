
class Node:
  def __init__(self, data):
    self.data = data 
    self.next = None 
    self.prev = None 

class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.length = 0

    def enqueue(self, data):
        node = Node(data)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.head.next = None
            self.length += 1
            
        elif self.length == 1:
            self.tail = node
            self.head.next = node
            self.length += 1 
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1

        

    def dequeue(self):
        if self.head == None:
            return 'erro'
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        if self.length > 1:
            temp = self.head 
            self.head = self.head.next
            self.length -= 1
        

    def print(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next
            # itr = itr.next        
            # self.head = self.head.next

        # if self.tail == None:  

# 'roberto', 'douglas'
q = Queue()
q.dequeue()
q.enqueue('roberto')
q.print()
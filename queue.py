class Node:
  def __init__(self, timestamp, valor):
    self.timestamp = timestamp
    self.valor = valor
    self.next = None 
    self.prev = None 

class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None

    def enqueue(self, timestamp, valor):
        node = Node(timestamp, valor)
        if self.head == None:
            self.head = node
            self.tail = node
            self.head.next = None

        elif not self.head.next:
            self.tail = node
            self.head.next = node

        else:
            self.tail.next = node
            self.tail = node
            
    def print(self):
        itr = self.head
        while itr:
            print(itr.valor, 'VALOR', itr.timestamp, 'HORA')
            itr = itr.next

# 'roberto', 'douglas'
q = Queue()
q.enqueue('2', 123)
q.enqueue('4', 321)
q.enqueue('1', 456)
q.enqueue('6', 789)
q.print()
#add: adiciona, 
#calcula: o valor gasto nas transações entre os timestamps dados
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
            
    def print(self, inicio, fim):
        itr = self.head
        valor = 0
        quantidade = 0
        while itr:
            if itr.timestamp >= inicio and itr.timestamp <= fim:
                quantidade += 1
                valor += itr.valor
                if itr.next == None:
                    print(quantidade, valor)
                    return
            else:
                print(quantidade, valor)
                return
            itr = itr.next   
    
    
    
    
    
    
    
    
    
q = Queue()
entradas = int(input())

for x in range(entradas):
  entrada = input().split()
  if entrada[0] == 'ADD':
    timestamp, valor = int(entrada[1]), int(entrada[2])
    q.enqueue(timestamp, valor)
  else:
    inicio, fim = int(entrada[1]), int(entrada[2])
    q.print(inicio, fim)
    
  
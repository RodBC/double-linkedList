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

    def days_to_sell(self, days):
        itr = self.tail
        prevItr = self.tail
        if itr.prev and itr.data < itr.prev.data:
            return 1
        while prevItr.prev:
            if itr.data >= prevItr.prev.data:
                days += 1
                prevItr = prevItr.prev
            else:
                return days
        return days
        
n_commands = int(input()) # ex:20
linkedList = DoublyLinkedList()
for x in range(n_commands):
  entrada = input().split()
  if entrada[0]!= 'INFO':
    valor = entrada[1]
    linkedList.push_back(int(entrada[1]))
    days = linkedList.days_to_sell(1)
    
  else:
    print(f'O ULTIMO VALOR FOI {valor} E HOJE E UM BOM DIA PARA VENDER ACOES DOS ULTIMOS {days} DIAS')
    

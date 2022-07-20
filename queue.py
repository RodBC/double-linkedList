class Q:
    def __init__(self):
        self.front = None
        self.rear = None
        self.nums = None
    def circular(self, initialValue):
        self.front = self.rear = -1
        self.nums = initialValue
        print(self.rear)
queue = Q()

a = 1
b = 2
pausa = a < 2
print(pausa)
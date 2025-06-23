class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_enqueue = []  
        self.stack_dequeue = []

    def enqueue(self, x):
        self.stack_enqueue.append(x)

    def dequeue(self):
        self._transfer()
        if self.stack_dequeue:
            self.stack_dequeue.pop()

    def front(self):
        self._transfer()
        if self.stack_dequeue:
            print(self.stack_dequeue[-1])
    
    def _transfer(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())


if __name__ == "__main__":
    q = QueueUsingTwoStacks()
    queries = int(input())
    for _ in range(queries):
        query = input().split()
        if query[0] == '1':
            q.enqueue(int(query[1]))
        elif query[0] == '2':
            q.dequeue()
        elif query[0] == '3':
            q.front()

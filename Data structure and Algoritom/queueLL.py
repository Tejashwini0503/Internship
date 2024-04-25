class Node:
    def _init_(self,data):
        self.data=data
        self.rear=None

class QueueLinkedList:
    def _init_(self):
        self.front = None

    def is_empty(self):
        return self.front is None
    def enqueue(self,item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeued_item
        else:
            raise IndexError("dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.front.data
        else:
            raise IndexError('peek from an empty queue')

    def size(self):
        count=0
        current=self.front
        while current:
            count+=1
            current=current.next
        return count
queue=QueueLinkedList()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue(5)
queue.dequeue(4)
queue.dequeue(6)
print('front of the queue:',queue.peek())
print('dequeue:',queue.dequeue())
print('size of the queue',queue.size())
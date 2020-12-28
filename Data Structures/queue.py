# FIFO structure: first item we insert is the first one we take out
class Queue():
    def __init__(self):
        self.queue = []

    # O(1) running time
    def is_empty(self):
        return self.queue == []

    # O(1) running time complexity
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) linear running time since we have to shift the remaining items. This is why we like linked lists, especially doubly linked lists
    def dequeue(self):
        if self.is_empty():
            return
        data = self.queue[0]
        del self.queue[0]

        return data

    # O(1) complexity
    def peek(self):
        if self.is_empty():
            return

        return self.queue[0]

    def size_queue(self):
        return len(self.queue)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(f"Size is: {queue.size_queue()}")
    queue.dequeue()
    print(f"Size is: {queue.size_queue()}")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(f"Size is: {queue.size_queue()}")

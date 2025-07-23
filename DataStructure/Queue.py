class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.__items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.__items[0]

    def size(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)
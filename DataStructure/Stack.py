class Stack:
    def __init__(self):
        self.__items = []
 
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.__items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.__items[-1]

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)
    
    def copy_to_list(self):
        return self.__items.copy()

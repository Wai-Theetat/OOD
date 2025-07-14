class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped = self.top.value
        self.top = self.top.next
        self._size -= 1
        return popped

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def __str__(self):
        items = []
        current = self.top
        while current:
            items.append(current.value)
            current = current.next
        return str(items)

def precedence(op):
    if op == '+':
        return 1
    elif op == '*':
        return 2
    return 0

def infxToPostfx(infx):
    res = []
    st = Stack()
    i = 0

    while i < len(infx):
        ch = infx[i]
        if ch.isalnum():  # Operand
            res.append(ch)
        elif ch in "+*":  # Operator
            while (not st.is_empty()) and precedence(st.peek()) >= precedence(ch):
                res.append(st.pop())
            st.push(ch)
        i += 1

    while not st.is_empty():
        res.append(st.pop())

    return ''.join(res)

def main():
    infx = "a*b+c"
    postfx = infxToPostfx(infx)
    print("Postfix:", postfx)

main()


#class Stack:
#    def __init__(self):
#        self.items = []

#    def push(self, item):
#        self.items.append(item)

#    def pop(self):
#        if self.is_empty():
#            raise IndexError("pop from empty stack")
#        return self.items.pop()

#    def peek(self):
#        if self.is_empty():
#            return None
#        return self.items[-1]

#    def is_empty(self):
#        return len(self.items) == 0

#    def size(self):
#        return len(self.items)

#    def __str__(self):
#        return str(self.items)
class Node:
    def __init__(self, value):
        self.__value = value
        self.next = None

    @property
    def value(self):
        return self.__value
    
    def __str__(self):
        return self.__value
class Stack:
    def __init__(self,size,  list = None):
        self.maxSize = size
        if list == None:
            self.items =[]
        else:
            self.items = list
        return
    
    def push(self, value):
        if self.size() < self.maxSize:
            self.items.append(value)
        return
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def isExist(self, value):
        return value in self.items
    
    def __str__(self):
        return str(self.items)
    
    def isFull(self):
        return self.size() == self.maxSize
    @property
    def clear(self):
        self.items.clear()   
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def append(self, value):
        newNode = Node(value)
        
        self.size += 1
        if(self.head == None):
            self.head = newNode
            return True
        
        focusNode = self.head
        while focusNode.next != None:
            focusNode = focusNode.next
        focusNode.next = newNode
        return True
    def pop(self):
        focus = self.head
        if self.isEmpty():
            return
        if self.size == 1:
            self.head = None
            self.size -= 1
            return
        while focus.next.next is not None:
            focus = focus.next
        print(focus.value)
        self.size -= 1
        focus.next = None
        return
        
    def removeAt(self, index):
        if self.isEmpty() or index < 0 or index >= self.size:
            return False   # handle invalid
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        focusNode = self.head
        for _ in range(index-1):
            focusNode = focusNode.next
        focusNode.next = focusNode.next.next
        self.size -= 1
        return True
        
    def isEmpty(self):
        return self.head == None
    
    def getAt(self, index):
        focusNode = self.head
        if self.isEmpty():
            return
        i = 0
        if index == 0:
            return focusNode
        while focusNode is not None and index > i:
            focusNode = focusNode.next
            i += 1
        return focusNode
    def insert(self, index, value):
        newNode = Node(value)
        focusNode = self.head
        self.size += 1
        if index == 0:
            newNode.next = focusNode
            self.head = newNode
            return True
        if self.isEmpty() and index > 0:
            return False
        if self.size < index or index < 0:
            return False
        
        i = 0

        while focusNode.next != None and index - 1 > i:
            focusNode = focusNode.next
            i += 1

        newNode.next = focusNode.next
        focusNode.next = newNode
        return True
    
    def __str__(self):
        ans = []
        node = self.head
        while node != None:
            ans.append(str(node.value))
            node = node.next
        if len(ans) > 0:
            return ' → '.join(ans)
        return "Empty"
    
def main():
    print(" *** Ant Army ***")
    ip, k = input("Input : ").split(",")
    
    ants = list(map(int, ip.split()))
    link = LinkedList()
    
    for i in ants:
        i = int(i)
        link.append(i)
    k = int(k)
    
    print(f"Before : {link}")
    
    index = 0
    length = link.size
    
    if k > link.size:
        k = link.size
        
    skip = False
    
    while index < length:
        
        stack = Stack(k)
        
        if not skip:
            for i in range(k - 1, -1, -1):
                
                if i + index > link.size:
                    continue
                node = link.getAt(i + index)
                stack.push(node)
                
                link.removeAt(i + index)
            
            while not stack.isEmpty():
                if stack.peek() is not None:
                    link.insert(index ,stack.pop().value)
                else:
                    stack.pop()
        # if k == 0:
        #     index += 1
        index += 1 if k == 0 else k
        skip = not skip
    print(f"After : {link}")
                
        


main()
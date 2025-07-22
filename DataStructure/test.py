class Stack:
    def __init__(self, list = None):
        if list == None:
            self.__items = []
        else:
            self.__items = list
        self.__size = len(self.__items)
        self.__poisoned = False

    def push(self,data):
        self.__items.append(data)
        self.__size += 1
        return
    
    def getSize(self):
        return self.__size
    
    def pop(self):
        self.__size -= 1
        return self.__items.pop()
    
    def peek(self): #ใช้ดู top of stack
        return self.__items[-1]

    def isEmpty(self):
        return self.__items == []
    
    def Base(self):
        for i in range(self.__size):
            self.__items[i] = -1
    
    def getPoison(self):
        self.__poisoned = True
        return
    
    def getPoisonlist(self):
        poisonlist = list(map(int, self.__items.copy()))
        length = len(poisonlist)
        i = 0
        while i < length:
            if poisonlist[i] % 2 == 0:
                poisonlist[i] -= 1
            else:
                poisonlist[i] += 2
            if poisonlist[i] < 1 : poisonlist[i] = 1
            i += 1
        return list(map(str, poisonlist))

    def observe(self):
        count = 0
        list1 = Stack()
        if self.__poisoned:
            for i in self.getPoisonlist():
                if list1.isEmpty(): 
                    list1.push(i)
                    continue
                while not list1.isEmpty() and list1.peek() <= i:
                    list1.pop()
                list1.push(i)
        else:
            for i in self.__items:
                if list1.isEmpty(): 
                    list1.push(i)
                    continue
                while not list1.isEmpty() and list1.peek() <= i:
                    list1.pop()
                list1.push(i)
        count = list1.getSize()
        self.__poisoned = False
        return count          
    
    def __str__(self):
        return f"list is {self.__items}"\
        
def process(data, stack):
    
    for i in data:
        action = i.split()
        if action[0] == "A":
            height = action[1]
            if height < "1":
                height = "1"
            stack.push(height)
            
        elif action[0] == "B":
            print(stack.observe())
            
        elif action[0] == "S":
            stack.getPoison()

def main():
    res = input("Enter Input : ").split(",")
    tree = Stack()
    process(res, tree)
    return

main()
class Node:
    def __init__(self, data):
        self.__data = data
        self.__left = self.__right = None
        self.__height = 1
        
    def gdata(self): return self.__data
    def sdata(self, data): self.__data = data
    
    def gleft(self): return self.__left
    def sleft(self, left): self.__left = left

    def gright(self): return self.__right
    def sright(self, right): self.__right = right

    def gheight(self): return self.__height
    def sheight(self, height): self.__height = height
    
    def isLT(self, data): return data < self.__data
    
class AVL:
    def __init__(self):
        self.__root = None
        
    def insert(self, data, currentNode = None, depth = 0):
        #print(depth)
        if(self.__root == None):
            self.__root = Node(data)
            return self.__root
        
        if(currentNode == None and depth == 0): 
            currentNode = self.__root
        
        if data < currentNode.gdata():
            if currentNode.gleft() is None:
               currentNode.sleft(Node(data))
            else:
               currentNode.sleft(self.insert(data, currentNode.gleft(), depth + 1))
        else:
            if currentNode.gright() is None:
               currentNode.sright(Node(data))
            else:
               currentNode.sright(self.insert(data, currentNode.gright(), depth + 1))
        
        self.setHeight(currentNode)
        currentNode = self.rebalance(currentNode)
        
        #if(currentNode == None): return
        
        #if(currentNode.isLT(data)):
        #    if(currentNode.gleft() == None):
        #        currentNode.sleft(Node(data))
        #    else:
        #        self.insert(data, currentNode.gleft(), depth + 1)
        #else:
        #    if(currentNode.gright() == None):
        #        currentNode.sright(Node(data))
        #    else:
        #        self.insert(data, currentNode.gright(), depth + 1)
        ##currentNode.sheight(currentNode.gheight() + 1)
        #self.setHeight(currentNode)
        #currentNode = self.rebalance(currentNode)
        if(depth == 0): 
            self.__root = currentNode
        return currentNode

    def setHeight(self, node):
        a = self.getHeight(node.gleft())
        b = self.getHeight(node.gright())
        res = 1 + max(a, b)
        node.sheight(res)
        return res
    
    def getHeight(self, node): return -1 if(node == None) else node.gheight()
        
    def balanceValue(self, node): return self.getHeight(node.gleft()) - self.getHeight(node.gright()) 

    def rightRotate(self, node):
        leftNode = node.gleft()
        temp = leftNode.gright()
        
        #Rotate
        leftNode.sright(node)
        node.sleft(temp)
        
        # Update heights
        self.setHeight(node)
        self.setHeight(leftNode)
        
        return leftNode
    
    def leftRotate(self, node):
        rightNode = node.gright()
        temp = rightNode.gleft()
    
        # Rotate
        rightNode.sleft(node)
        node.sright(temp)
    
        # Update heights
        self.setHeight(node)
        self.setHeight(rightNode)
    
        return rightNode

    def rebalance(self, node):
        if(node == None): 
            return node

        balance = self.balanceValue(node)

        # RH
        if(balance < -2):
            #RL
            if(self.balanceValue(node.gright()) > -1):
                node.sright(self.rightRotate(node.gright()))
            node = self.leftRotate(node)
        
        # LH
        if(balance > 2):
            #LR
            if(self.balanceValue(node.gleft()) < 1):
                node.sleft(self.leftRotate(node.gleft()))
            node = self.rightRotate(node)
        
        return node
    
    def printTree(self):
        self._printTree(self.__root)
        print()

    def _printTree(self, node, level = 0):
        if (node != None):
            self._printTree(node.gright(), level + 1)
            print('     ' * level, node.gdata())
            self._printTree(node.gleft(), level + 1)
            
    def postOrder(self, node = None, depth = 0):
        if(node == None and depth == 0): node = self.__root
        if(node == None): return
        self.postOrder(node.gleft(), depth + 1)
        self.postOrder(node.gright(), depth + 1)
        print(node.gdata(), end = " ")
        
    
def main():
    avl1 = AVL()
    inp = input('Enter Input : ').split(',')

    for i in inp:
        print(i)
        if i[:2] == "AD":
            # print("AD")
            avl1.insert(int(i[3:]))
        elif i[:2] == "PR":
            # print("PR")
            avl1.printTree()
            # print("PO")
        elif i[:2] == "PO":
            avl1.postOrder()
            
main()
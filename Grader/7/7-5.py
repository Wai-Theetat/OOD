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

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.__val = val
		self.__left = left
		self.__right = right

	@property
	def val(self) : return self.__val
	@property
	def left(self) : return self.__left
	@property
	def right(self) : return self.__right

	@val.setter
	def val(self, new_val): self.__val = new_val
	@left.setter
	def left(self, new_node): self.__left = new_node
	@right.setter
	def right(self, new_node): self.__right = new_node

class BinaryTree:
	def __init__(self, root = None):
		self.__root = root
  
	@property
	def root(self) : return self.__root	
	
	def printTreeVisual(self,root, indent="", last='updown'):
		if root != None:
			print(indent, end='')
			if last == 'updown': 
				print("Root----", end='')
				indent += "       "
			elif last == 'right': 
				print("R----", end='')
				indent += "       "
			elif last == 'left': 
				print("L----", end='')
				indent += "       "
			print(root.val)
			self.printTreeVisual(root.left, indent, 'left')
			self.printTreeVisual(root.right, indent, 'right')

	def breadth_first_insert(self, lst):
		if not lst:
			return

		self.__root = TreeNode(lst[0])
		queue = Queue()
		queue.enqueue(self.__root)
		i = 1

		while i < len(lst):
			current = queue.dequeue()
			if i < len(lst):
				current.left = TreeNode(lst[i])
				queue.enqueue(current.left)
				i += 1
			if i < len(lst):
				current.right = TreeNode(lst[i])
				queue.enqueue(current.right)
				i += 1
  
	def mirror_at_depth(self, root, depth, toggle, current_depth = 0):
		if not root : return
  
		if (current_depth == depth) or toggle:
			#print('Pre',  root.left.val, root.right.val)
			toggle = True
			root.left, root.right = root.right, root.left
			#print('Post', root.left.val, root.right.val)

		self.mirror_at_depth(root.left, depth, toggle,current_depth + 1)
		self.mirror_at_depth(root.right, depth, toggle, current_depth + 1)

	def breadth_first_to_list(self):

		lst = []		
		queue = Queue()
		queue.enqueue(self.__root)

		while not queue.is_empty():
			node = queue.dequeue()
			lst.append(node.val)

			if node.left is not None:
				queue.enqueue(node.left)

			if node.right is not None:
				queue.enqueue(node.right)

		return lst

class Solution:
    
	def main(self):
		print(' *** Mirror Tree ***')
		lst_node, mirror_depth = input('Enter nodes in level-order,depth : ').split(',')
    
		lst_node = list(map(int,lst_node.split()))
		mirror_depth = int(mirror_depth)
		
		if mirror_depth == 0 : mirror_depth = 1
  
		tree = BinaryTree()
	
		print('before mirror:', lst_node)
		tree.breadth_first_insert(lst_node)
		tree.printTreeVisual(tree.root)
	
		tree.mirror_at_depth(tree.root,  mirror_depth-1, False)

		print('after mirror :', tree.breadth_first_to_list())
		tree.printTreeVisual(tree.root)
   
   
sol = Solution()
sol.main()
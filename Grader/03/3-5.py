class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def copy_items(self):
        return self.items[:]

def apply_mushroom_effect(tree_stack):
    temp = Stack()
    while not tree_stack.is_empty():
        val = tree_stack.pop()
        if val % 2 == 1:   
            val += 2
        else:              
            val -= 1
            val = max(val, 1)  # min is 1
        temp.push(val)

    # restore order
    tree_stack_restored = Stack()
    while not temp.is_empty():
        tree_stack_restored.push(temp.pop())
    return tree_stack_restored

def count_visible_trees(tree_stack):
    temp = Stack()
    max_height = 0
    cnt = 0
    while not tree_stack.is_empty():
        height = tree_stack.pop()
        if height > max_height:
            cnt += 1
            max_height = height
        temp.push(height)

    # restore original stack
    while not temp.is_empty():
        tree_stack.push(temp.pop())

    return cnt

def main():
    events = input("Enter Input : ").split(',')
    tree = Stack()
    mushroom_effect = False

    for event in events:
        if event.startswith('A'):
            _, val = event.split()
            tree.push(int(val))

        elif event == 'S':
            mushroom_effect = True

        elif event == 'B':
            if mushroom_effect:
                tree = apply_mushroom_effect(tree)
                mushroom_effect = False
            print(count_visible_trees(tree))

main()

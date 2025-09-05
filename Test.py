class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postfix_to_tree(postfix):
    stack = []
    for token in postfix:
        if token.isalnum():  # operand
            stack.append(Node(token))
        else:  # operator
            right = stack.pop()
            left = stack.pop()
            node = Node(token)
            node.left = left
            node.right = right
            stack.append(node)
    return stack[0]  # root of tree

# Example usage
def print_inorder(node):
    if node:
        print('(', end='')
        print_inorder(node.left)
        print(node.value, end='')
        print_inorder(node.right)
        print(')', end='')

expr = "ab+cde+**"
root = postfix_to_tree(expr)
print_inorder(root)

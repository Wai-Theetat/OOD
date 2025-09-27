import math

class BTreeNode:
    def __init__(self, is_leaf=True):
        self.__keys  = []
        self.__children = []
        self.__is_leaf = is_leaf

#===========Getter====================================
    def is_leaf(self): return self.__is_leaf
    def get_keys_size(self): return len(self.__keys)
    def get_keys(self): return self.__keys
    def get_key_at(self, index): return self.__keys[index]
    def get_children(self): return self.__children
    def get_child_at(self, index) -> 'BTreeNode' : return self.__children[index]
    def is_equal_to_current_size(self, value): return (self.get_keys_size() == value)

#============Setter====================================
    def add_key(self, key):
        i = 0
        while i < len(self.__keys) and self.__keys[i] < key:
            i += 1
        self.__keys.insert(i, key)

    def add_child(self, child):
        self.__children.append(child)

    def insert_key_at(self, index, key): self.__keys.insert(index, key)
    def remove_key_at(self, index): return self.__keys.pop(index)

    def insert_child_at(self, index, child): self.__children.insert(index, child)
    def remove_child_at(self, index): return self.__children.pop(index)


#===========Displayer=====================================
    def display(self, level=0, prefix="Root"):
        indent = "    " * level
        print(f"{indent}{prefix}: {self.__keys}")
        for i, child in enumerate(self.__children):
            if child.get_keys():  # Only display non-empty children
                child.display(level + 1, prefix=f"Child {i}")


class BTree:
    def __init__(self, max_children):
        self.__max_degree = max_children
        self.__max_keys = max_children - 1
        self.__min_keys = math.ceil(max_children / 2) - 1  # Correct minimum keys
        self.__root = BTreeNode(True)                   # Start as A leaf

    def insert(self, data):
        root = self.__root
        if root.is_equal_to_current_size(self.__max_keys):  # Root max keys case
            new_root = BTreeNode(False)                     # create a new root
            new_root.add_child(root)                        # old root becomes first child
            self.__seperate_child(new_root, 0)              # split the old root
            self.__root = new_root                          # update the tree's root
            self.__insert_non_full(new_root, data)
        else:
            self.__insert_non_full(root, data)

    def __insert_non_full(self, node : BTreeNode, key):
        if node.is_leaf(): node.add_key(key)
        else:
            i = node.get_keys_size() - 1                       # Start from most
            while i >= 0 and key < node.get_key_at(i):         # Traverse Back till current < key
                i -= 1
            i += 1                                             # Require i for later                                          
            child = node.get_child_at(i)
            if child.is_equal_to_current_size(self.__max_keys): # child already max
                self.__seperate_child(node, i)                  # Split it before recure with full child
                if key > node.get_key_at(i):
                    i += 1
            self.__insert_non_full(node.get_child_at(i), key)

    def __seperate_child(self, parent: BTreeNode, indx):
        full_child = parent.get_child_at(indx)
        new_child = BTreeNode(full_child.is_leaf())
        mid = self.__max_keys // 2

        # Move middle key up to parent
        parent.insert_key_at(indx, full_child.get_key_at(mid))

        # Left child keeps keys before mid
        left_keys = full_child.get_keys()[:mid]
        # Right child gets keys after mid
        right_keys = full_child.get_keys()[mid+1:]

        full_child.get_keys().clear()
        full_child.get_keys().extend(left_keys)
        new_child.get_keys().extend(right_keys)

        # If not leaf, move children as well
        if not full_child.is_leaf():
            left_children = full_child.get_children()[:mid+1]
            right_children = full_child.get_children()[mid+1:]
            full_child.get_children().clear()
            full_child.get_children().extend(left_children)
            new_child.get_children().extend(right_children)

        parent.insert_child_at(indx + 1, new_child)

    def display(self):
        self.__root.display()
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        new_val = Node(new_val)
        self.bst_insert(self.root, new_val)

    def bst_insert(self, base_node, new_val):
        
        if base_node.value > new_val.value:
            if base_node.left == None:
                base_node.left = new_val
            else:
                base_node = base_node.left
                self.bst_insert(base_node, new_val)
        elif base_node.value < new_val.value:
            if base_node.right == None:
                base_node.right = new_val
            else:
                base_node = base_node.right
                self.bst_insert(base_node, new_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root, "")

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def search(self, val):
        return self.binary_search(self.root, val)    

    def binary_search(self, base_node, val):
        if base_node:
            if base_node.value == val:
                return True
            elif base_node.value > val:
                print("ran left")
                return self.binary_search(base_node.left, val)
            elif base_node.value < val:
                print("ran right")
                return self.binary_search(base_node.right, val)
                
        return False
        

tree = BST(4)
# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree.print_tree())

print(tree.search(5))
print(tree.search(1))







class LinkedBinaryTree:
    """A binary tree implementation using a linked structure."""

    class _Node:
        """A nested class representing a node in the binary tree."""

        __slots__ = 'element', 'parent', 'left', 'right'

        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right
        
        def __eq__(self, other):
            return type(other) is type(self) and other.element is self.element

    def __init__(self):
        """Create an empty binary tree."""
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def rootm(self):
        return self.root
    
    def parent(self, n):
        return n.parent

    def insert(self, value):
        if self.root is None:
            self.root = self._Node(value)
            self.size = 1
        else:
            self._insert_recursively(self.root, value)
    
    def _insert_recursively(self, node, value):
        if value < node.element:
            if node.left is None:
                node.left = self._Node(value)
                node.left.parent = node
                self.size += 1
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = self._Node(value)
                node.right.parent = node
                self.size += 1
            else:
                self._insert_recursively(node.right, value)
        

        # Preorder
    def preorder_traversal(self):
        result = []
        self._preorder_traversal_recursive(self.root, result)
        return result
    
    def _preorder_traversal_recursive(self, node, result: list):
        if node:
            result.append(node.element)
            self._preorder_traversal_recursive(node.left, result)
            self._preorder_traversal_recursive(node.right, result)
    
    def delete(self, node):
        pass
    
    def depth(self, p):
        if p == self.root:
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def num_of_children(self, node):
        if node is None:
            return 0
        child = 0
        if node.left is not None:
            child += 1
        if node.right is not None:
            child += 1

        left_child = self.num_of_children(node.left)
        right_child = self.num_of_children(node.right)

        e =  child + left_child+ right_child
        
        return e






T = LinkedBinaryTree()
T.insert(11)
T.insert(9)
T.insert(12)
T.insert(4)
T.insert(10)
T.insert(22)
T.insert(5)

# r = T.parent(node(4))
print(T.preorder_traversal())
print(T.num_of_children(T.rootm()))

# e = T.parent(T.rootm().left).element

# print(e)
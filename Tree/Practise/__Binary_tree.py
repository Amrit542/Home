
class Node():
    def __init__(self, k) -> None:
        self.value = k
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root  = Node(value)
        else:
            self._insert_recursive(self.root, value)
       
    
    def _insert_recursive(self, node : Node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    # Preorder
    def preorder_traversal(self):
        result = []
        self._preorder_traversal_recursive(self.root, result)
        return result
    
    def _preorder_traversal_recursive(self, node, result: list):
        if node:
            result.append(node.value)
            self._preorder_traversal_recursive(node.left, result)
            self._preorder_traversal_recursive(node.right, result)


    # Inorder
    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result
    
    def _inorder_traversal_recursive(self, node, result: list):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.value)
            self._inorder_traversal_recursive(node.right, result)


    # Postorder
    def postorder_traversal(self):
        result = []
        self._postorder_traversal_recursive(self.root, result)
        return result
    
    def _postorder_traversal_recursive(self, node, result):
        if node:
            self._postorder_traversal_recursive(node.left, result)
            self._postorder_traversal_recursive(node.right, result)
            result.append(node.value)



    
    def root1(self):
        return self.make_position(self.root)
    
    

    

    def search(self, node, key):
        if not node:
            return False
        elif node.value == key:
            return True
        elif node.value < key:
            return self.search(node.right, key)
        else:
            return self.search(node.left, key)

    def successor(self, node):
        succParent = node

        succ = node.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
        # print(succParent.value)
        print(succ.value)
        return (succParent, succ)
    
    def delete(self, node, key):
        # x = self.search(self.root, key)
        # if not x:
        #     print('Not exists key {}'.format(key))
        if not node:
            return node
        elif key < node.value:
            node.left = self.delete(node.left, key)
        elif key > node.value:
            node.right = self.delete(node.right, key) 
        else:
            # One children
            if not node.right:
                return node.left
            elif not node.left:
                return node.right
            
            # for 2 children
            (succParent, succ) = self.successor(node)
            node.value = succ.value
            node.right = self.delete(node.right, succ.value)


        return node

    def searchBST(self, root, val):
        if  root is not None and root.value == val:
            return root
        elif val < root.value:
            return self.searchBST(root.left, val)
        elif val > root.value:
            return self.searchBST(root.right, val)
        else:
            return None
    
    def isvalid_BST(self, root):
        stack = []
        prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and prev.value >= root.value:
                return False
            prev = root
            root = root.right
        return True

            
 


tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)
tree.insert(58)
tree.insert(59)



# print(tree.postorder_traversal())
# print(tree.search(tree.root, 84))
# print(tree.successor(tree.root))

# print(tree.inorder_traversal())
# tree.delete(tree.root, 30)
# tree.delete(tree.root, 50)
# tree.delete(tree.root, 40)
# print(tree.inorder_traversal())
r = tree.searchBST(tree.root, 30)
print(tree.isvalid_BST(tree.root))


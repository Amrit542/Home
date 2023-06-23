class Node():
    def __init__(self, value, l = None, r = None):
        self.value = value
        self.left = l
        self.right = r

class ExpressionTree():

    # def build_tree(self, data):
    #     stack = []
    #     for t in data:

    #         if t in '+-*/':
    #             stack.append(t)
    #         elif t not in '()':
    #             stack.append(ExpressionTree(t))
    #         elif t == ')':

    #             right = stack.pop()
    #             op = stack.pop()
    #             left = stack.pop()
    #             stack.append(ExpressionTree(op, left, right))
    #     print(stack)
    #     self.root = stack[0]
    #     print(self.root.left.value)

    #     return stack.pop()
    def build_expression_tree(self, tokens: str):
        stack = []
        for t in tokens:
            if t in '+-*/':
                stack.append(t)
            elif t not in '()':
                stack.append(Node(t))
            elif t == ')':
                right = stack.pop()
                o = stack.pop()
                left = stack.pop()
                node = Node(o, left, right)
                stack.append(node)
        # e = self.print_inorder(stack[0])
        # ev = self._evaluate_expression(stack[0])
        # e = stack[0].right.value
        self.root = stack[0]
        print(stack)
        return stack.pop()
    
    def print_inorder(self):
        s = []
        
        self._inorder(self.root, s)
        print(s)
        return
        

    def _inorder(self, node, result : list):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

  



s = '(((5 + 2) * (2-1)) / ((2+9) +((7-2) -1))*8)'

n = s.replace(' ', '')
print(n)
T = ExpressionTree()
T.build_expression_tree(n)
T.print_inorder()
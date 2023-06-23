class Node():
    def __init__(self, value, l = None, r = None):
        self.value = value
        self.left = l
        self.right = r

class ExpreesionTree():

    def evaluate(self):
        return self._evaluate_expression()
    
    def _evaluate_expression(self, node):
        if node.left is None or node.right is None:
            return node.value
        
        else:
            op = node.value
            left_value = int(self._evaluate_expression(node.left))
            right_value = int(self._evaluate_expression(node.right))
            if op == '+': return left_value + right_value
            elif op == '-': return left_value - right_value
            elif op == '*': return left_value * right_value
            else: return left_value / right_value
    


    

            # Preorder
    def preorder_traversal(self):
        result = []
        self._preorder_traversal_recursive(self.root, result)
        return result
    
    def _preorder_traversal_recursive(self, node, result: list):
        if node:
            self._preorder_traversal_recursive(node.left, result)
            result.append(node.value)
            self._preorder_traversal_recursive(node.right, result)
    
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
        e = self.print_inorder(stack[0])
        ev = self._evaluate_expression(stack[0])
        # e = stack[0].right.value
        print(ev)
        return stack.pop()
         
    def print_inorder(self, node):
      result = []
      self._preorder_traversal_recursive(node, result)
      print(result)
      return result



s = '(((3+1)*4)/((9-5)+2))'
t = ExpreesionTree()
t.build_expression_tree(s)
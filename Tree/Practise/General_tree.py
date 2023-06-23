class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        self.child = child
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1

        return level
    
    def print_tree(self):
        print(str(' '*self.get_level()) + '|--', end = '')
        print(self.data)
        if self.children:
            for each in self.children:
                each.print_tree()

    def indent(self, node, depth = 0):
        if node is not None:
            print(' '* depth + node.data)
            for e in node.children:
                self.indent(e, depth +1)



root = TreeNode("Eletronics")
laptop = TreeNode("Laptop")
root.add_child(laptop)

laptop.add_child(TreeNode("Mac"))
laptop.add_child(TreeNode("Windows"))
laptop.add_child(TreeNode("Linux"))

tv = TreeNode('TV')
root.add_child(tv)
tv.add_child(TreeNode('LG'))
tv.add_child(TreeNode('Samsung'))
tv.add_child(TreeNode('Apple'))

root.print_tree()


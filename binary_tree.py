class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self, root):
        self.root = Node(root)
        
    def preorder(self, start, records):
        if start is not None:
            records.append(start.value)
            records = self.preorder(start=start.left, records=records)
            records = self.preorder(start=start.right, records=records)

        return records
    
    def postorder(self, start, records): # 2 ->
        if start is not None:
            records = self.postorder(start=start.left, records=records)
            records = self.postorder(start=start.right, records=records)
            records.append(start.value)

        return records
    
tree = Tree(5)
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(2)
tree.root.left.right = Node(8)

print(tree.postorder(tree.root, []))
    
#       5
#      / \
#     3   4
#    / \  
#   2   8 
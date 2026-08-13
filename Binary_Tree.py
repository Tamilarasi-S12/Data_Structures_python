class Node:
    def __init__(self, title):
        self.title = title
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, title):
        new_node = Node(title)
        if self.root is None:
            self.root = new_node
            return
        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.title)
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.title)
            self.preorder(node.left)
            self.preorder(node.right)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.title)
tree = BinaryTree()
n = int(input("Enter number of books: "))
for i in range(n):
    title = input("Enter book title: ")
    tree.insert(title)
print("Inorder Traversal:")
tree.inorder(tree.root)
print("Preorder Traversal:")
tree.preorder(tree.root)
print("Postorder Traversal:")
tree.postorder(tree.root)

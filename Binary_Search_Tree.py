class Node:
    def __init__(self, name, time, purpose):
        self.name = name
        self.time = time
        self.purpose = purpose
        self.left = None
        self.right = None
      
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, name, time, purpose):
        new_node = Node(name, time, purpose)
        if self.root is None:
            self.root = new_node
            return
            current = self.root
        while True:
            if time < current.time:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, time):
        current = self.root
        while current is not None:
            if time == current.time:
                return current
            elif time < current.time:
                current = current.left
            else:
                current = current.right
        return None

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
  
  def delete(self, node, time):
        if node is None:
            return None
        if time < node.time:
            node.left = self.delete(node.left, time)
        elif time > node.time:
            node.right = self.delete(node.right, time)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            minimum = self.find_min(node.right)
            node.name = minimum.name
            node.time = minimum.time
            node.purpose = minimum.purpose
            node.right = self.delete(node.right, minimum.time)
        return node
    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(
                node.name,
                "|",
                node.time,
                "|",
                node.purpose
            )
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(
                node.name,
                "|",
                node.time,
                "|",
                node.purpose
            )
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)

            print(
                node.name,
                "|",
                node.time,
                "|",
                node.purpose
            )

    def count(self, node):
        if node is None:
            return 0
        return (
            1
            + self.count(node.left)
            + self.count(node.right)
        )

tree = BinaryTree()
n = int(input("Enter number of visitors: "))
for i in range(n):
    print("\nEnter visitor", i + 1, "details")
    name = input("Enter visitor name: ")  
    time = input("Enter entry time (HH:MM): ")
    purpose = input("Enter purpose: ")
    tree.insert(name, time, purpose)
    print("Visitor inserted successfully.")
print(" == LOG BOOK ==")
print("1. Search Visitor")
print("2. Display Visitors")
print("3. Delete Visitor")
print("4. Count Total Visitors")
print("5. Exit")

while True:
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a number from 1 to 5.")
        continue
    if choice == 1:
        time = input(
            "Enter entry time to search (HH:MM): "
        )
        result = tree.search(time)
        if result is not None:

            print("\n----- Visitor Found -----")
            print("Visitor Name :", result.name)
            print("Entry Time   :", result.time)
            print("Purpose      :", result.purpose)
        else:
            print("\nVisitor not found.")
    elif choice == 2:
        if tree.root is None:
            print("\nNo visitors available.")
            continue
        print("\n--- INORDER TRAVERSAL ---")
        tree.inorder(tree.root)
        print("\n--- PREORDER TRAVERSAL ---")
        tree.preorder(tree.root)
        print("\n--- POSTORDER TRAVERSAL ---")
        tree.postorder(tree.root)
    elif choice == 3:
        time = input(
            "Enter entry time to delete (HH:MM): "
        )
        result = tree.search(time)
        if result is not None:
            tree.root = tree.delete(
                tree.root,
                time
            )
            print("\nVisitor deleted successfully.")
        else:
            print("\nVisitor not found.")
    elif choice == 4:
        total = tree.count(tree.root)
        print("\nTotal visitors:", total)
    elif choice == 5:
        print("\nProgram ended.")
        break  
    else:
        print("\nInvalid choice. Please enter 1 to 5.")

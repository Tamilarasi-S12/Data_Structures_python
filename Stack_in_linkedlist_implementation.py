class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, max_size):
        self.top = None
        self.max_size = max_size
        self.current_size = 0

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return self.current_size >= self.max_size

    def push(self, data):
        if self.is_full():
            print("Stack Overflow! Cannot push.")
            return
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.current_size += 1
        print(f"Pushed {data} into the stack.")

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_data = self.top.data
        self.top = self.top.next
        self.current_size -= 1
        return popped_data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        print("Stack elements (top to bottom):")
        while current:
            print(current.data)
            current = current.next

size = int(input("Enter size of the stack: "))
stack = Stack(size)

print("\n--- Stack Operations ---")
print("1. Push")
print("2. Pop")
print("3. Peek")
print("4. Display")
print("5. Exit")

while True:
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        value = input("Enter data to push: ")
        stack.push(value)
    elif choice == "2":
        result = stack.pop()
        print(f"Popped value: {result}")
    elif choice == "3":
        result = stack.peek()
        if result is None:
            print("Stack is empty.")
        else:
            print(f"Top element: {result}")
    elif choice == "4":
        stack.display()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please select between 1 and 5.")

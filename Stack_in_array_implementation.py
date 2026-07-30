class Stack: 
    def __init__(self, max_size): 
        self.stack = [] 
        self.max_size = max_size 
        
    def push(self, item): 
        if len(self.stack) >= self.max_size: 
            print("Stack is full") 
            return 
        self.stack.append(item) 
        print(f"{item} pushed to stack") 
        
    def pop(self): 
        if self.is_empty(): 
            return "Stack Underflow" 
        return self.stack.pop() 
        
    def peek(self): 
        if self.is_empty(): 
            return "Stack is Empty" 
        return self.stack[-1] 
        
    def is_empty(self): 
        return len(self.stack) == 0 
        
    def size(self): 
        return len(self.stack) 
        
    def display(self): 
        print("Stack elements:", self.stack) 

s = int(input("Enter the size of the stack: ")) 
array = Stack(s) 

 
print("\n--- Stack Operations Menu ---") 
print("1. Push") 
print("2. Pop") 
print("3. Peek") 
print("4. Display") 
print("5. Size") 
print("6. Exit") 

while True: 
    choice = input("\nEnter your choice (1-6): ") 
    match choice: 
        case '1': 
            item = input("Enter an element to push: ") 
            array.push(item) 
        case '2': 
            removed_element = array.pop() 
            if removed_element == "Stack Underflow": 
                print(removed_element) 
            else: 
                print(f"Element {removed_element} is popped") 
        case '3': 
            print("The top element in stack:", array.peek()) 
        case '4': 
            array.display() 
        case '5': 
            print("The size of the stack:", array.size()) 
        case '6': 
            print("Exiting program.") 
            break 
        case _: 
            print("Invalid choice! Please choose between 1 and 6.")

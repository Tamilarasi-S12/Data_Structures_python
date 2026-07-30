class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        print("Queue:", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


queue = Queue()

print("\n--Queue Operations--")
print("1. Enqueue")
print("2. Dequeue")
print("3. Peek")
print("4. Size")
print("5. Display")
print("6. Exit")

while True:

    ch = input("Enter your choice: ")

    if ch == "1":
        data = input("Enter element: ")
        queue.enqueue(data)
        print("Element enqueued.")

    elif ch == "2":
        item = queue.dequeue()
        if item is None:
            print("Queue is empty")
        else:
            print("Dequeued element:", item)

    elif ch == "3":
        item = queue.peek()
        if item is None:
            print("Queue is empty")
        else:
            print("Front element:", item)

    elif ch == "4":
        print("Queue size:", queue.size())

    elif ch == "5":
        queue.display()

    elif ch == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, value):
        if len(self.queue) == self.size:
            print("Queue Overflow")
        else:
            self.queue.append(value)
            print(value, "enqueued")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow")
        else:
            print(self.queue.pop(0), "dequeued")

    def display(self):
        print("Queue:")
        for i in self.queue:
          print(i)


size = int(input("Enter queue size: "))
q = Queue(size)

print("1. Enqueue")
print("2. Dequeue")
print("3. Display")
print("4. Exit")

while True:
    choice = int(input("\nEnter your choice: "))

    match choice:
        case 1:
            value = int(input("Enter value: "))
            q.enqueue(value)

        case 2:
            q.dequeue()

        case 3:
            q.display()

        case 4:
            print("Exiting...")
            break

        case _:
            print("Invalid choice")

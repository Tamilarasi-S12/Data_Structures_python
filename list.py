n = int(input("Enter number of elements:"))
l = []
for i in range(n):
    a = int(input(f"Enter the element {i+1}:"))
    l.append(a)
print("Positive elements in the list are:")
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > 0 and l[j] > 0:
            print((l[i], l[j]))

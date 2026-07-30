class Node :
    def __init__(self,coeff,exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None
class Polynomial :
    def __init__(self):
        self.head = None
    def insert(self,coeff,exp):
        new_node = Node (coeff,exp)
        if not self.head or self.head.exp < exp:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next and temp.next.exp > exp:
            temp = temp.next
        if temp.exp ==exp:
            temp.coeff += coeff
        elif temp.next and temp.next.exp == exp:
            temp.next.coeff += coeff
        else :
            new_node.next = temp.next
            temp.next = new_node
    def add(poly1,poly2):
        p = poly1.head
        q = poly2.head
        res = Polynomial()
        while p and q:
            if p.exp == q.exp :
                res.insert(p.coeff+q.coeff,p.exp)
                p = p.next
                q = q.next
            elif p.exp > q.exp :
                res.insert(p.coeff,p.exp)
                p = p.next
            else :
                res.insert(q.coeff,q.exp)
                q=q.next
        while p:
            res.insert(p.coeff,p.exp)
            p = p.next
        while q:
            res.insert(q.coeff,q.exp)
            q = q.next
        return res
    def display (self):
        if self.head is None:
            print ("0")
            return
        temp = self.head
        while temp :
            print(f"{temp.coeff}x^{temp.exp}",end = " ")
            if temp.next:
                print("+",end= " ")
            temp = temp.next
        print()
poly1 = Polynomial()
poly2 = Polynomial()
n1= int(input("Enter number of terms in first polynomial:"))
n2 = int(input("Enter number of terms in second polynomial:"))
print ("First polynomial")
for i in range (n1):
    c= int(input("Enter coefficient"))
    e= int(input("Enter power:"))
    poly1.insert(c,e)
print ("Second Polynomial")
for i in range (n2):
    c= int(input("Enter coefficient"))
    e= int(input("Enter power:"))
    poly2.insert(c,e)
print("Polynomial 1 :")
poly1.display()
print("Polynomial 2 :")
poly2.display()
print ("Polynomial Addition:")
sum_poly = Polynomial.add(poly1,poly2)
sum_poly.display()             

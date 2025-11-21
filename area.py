class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b



l1 = int(input("Enter length of first rectangle: "))
b1 = int(input("Enter breadth of first rectangle: "))
l2 = int(input("Enter length of second rectangle: "))
b2 = int(input("Enter breadth of second rectangle: "))


r1 = Rectangle(l1, b1)
r2 = Rectangle(l2, b2)


if r1.area() > r2.area():
    print("First rectangle is larger.")
elif r1.area() < r2.area():
    print("Second rectangle is larger.")
else:
    print("Both are equal.")

~                                                                                                                                                       
~                                                                                                                                                       
~       

class Complex:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __str__(self):
       return f" ({self.a} + {self.b}i)"

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


a1=Complex(1,3)
a2=Complex(3,5)

print(a1)
print(a2)
print(a1+a2)
print(a1*a2)
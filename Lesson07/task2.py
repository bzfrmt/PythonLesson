from abc import ABC, abstractmethod
class Wear(ABC):
    w=0
    h=0

    def __init__(self,h=0,w=0):
        self.h=h
        self.w=w

    @abstractmethod
    def square(self):
        return self.h*self.w/14

class Coat(Wear):
    @property
    def square(self):
        return self.w/6.5 + 0.5

class Suit(Wear):
    @property
    def square(self):
        return self.h*2+0.3


w1=Coat(1.65,48)
print(f"{w1.square:.2f} м2")

w2=Suit(1.65,48)
print(f"{w2.square:.2f} м2")

print(f"{w1.square+w2.square:.2f} м2")
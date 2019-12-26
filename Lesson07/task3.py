class Cell:
    alveola=0
    def __init__(self,alveola=0):
        self.alveola=int(alveola)

    def __str__(self):
        return str(self.alveola)

    def __add__(self, other):
        result=self.alveola+other.alveola
        return Cell(result)

    def __sub__(self, other):
        if self.alveola>other.alveola:
            result=self.alveola-other.alveola
            return Cell(result)
        else:
            print(f"Ошибка вычитания {self.alveola} - {other.alveola}")
            return False

    def __mul__(self, other):
        result=self.alveola*other.alveola
        return Cell(result)

    def __truediv__(self, other):
        if other.alveola>0:
            result=self.alveola//other.alveola
            return Cell(result)
        else:
            print(f"Ошибка деления {self.alveola} / {other.alveola}")
            return False

    def make_order(self,n=0):
        result=""
        for i in range(self.alveola):
            result+="*"
            if n>0 and (i+1)//n==(i+1)/n:
                result+="\n"
        return result



c1=Cell(10)
c2=Cell(3)

print(f"Клетка1 содержит {c1} ячеек")
print(f"Клетка1 содержит {c2} ячеек")
print(f"Сложение c1+c2: Клетка содержит {c1+c2} ячеек")
print(f"Вычитание c1-c2: Клетка содержит {c1-c2} ячеек")
print(f"Вычитание c2-c1: Клетка содержит {c2-c1} ячеек")
print(f"Умножение c2*c1: Клетка содержит {c2*c1} ячеек")
print(f"Деление c1/c2: Клетка содержит {c1/c2} ячеек")
print(c1.make_order(4))
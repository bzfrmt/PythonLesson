class Worker:
    name=""
    surname=""
    position=""
    _income={"wage": 0, "bonus": 0}

    def __init__(self):
        self.name=input("Введите Имя: ")
        self.surname=input("Введите Фамилию: ")
        self._income["wage"]=int(input("Введите оклад: "))
        self._income["bonus"]=int(input("Введите премию: "))
        
    def print_worker():
        print (f"{self.name} {self.surname}")
        print (f'Оклад:{self._income["wage"]} Премия:{self._income["bonus"]}')

class Position(Worker):
    full_name=""
    _total_income=0

    def get_full_name(self):
            self.full_name=str(self.name)+" "+str(self.surname)

    def get_total_income(self):
            self._total_income=int(self._income["wage"])+int(self._income["bonus"])

p=Position()
#p.name="Иван"
#p.surname="Иванов"
#p.position="специалист"
#p._income["wage"]=10000
#p._income["bonus"]=5000

p.get_total_income()
p.get_full_name()
print(p.full_name)
print(p._total_income)
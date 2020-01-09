class Tech:
    width=0
    height=0
    lenght=0
    type="tech"
    id=""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.id=brand+"_"+model
    def __str__(self):
        return f"Tech: {self.type} {self.brand} {self.model}"

class Printer(Tech):
    type="printer"
    colors=1
    def to_print(self):
        print(f"{self.type} {self.brand} {self.model} печатает всеми {self.colors} цветами")

class Xerox(Tech):
    type="xerox"
    copies=1
    def to_xerox(self):
        print(f"{self.type} {self.brand} {self.model} делает {self.copies} копий в минуту")

class Scaner(Tech):
    type="scaner"
    scans=1
    def to_scan(self):
        print(f"{self.type} {self.brand} {self.model} делает {self.scans} сканов в минуту")

class Storage:
    def __init__(self, name):
        self.name = name
        self.storage_dict={}

    def __str__(self):
        return f"Склад: {self.name} имеет {self.storage_dict}"

    def my_list(self):
        return self.storage_dict

    def to_get(self,tech):
        result=0
        try:
            result=self.storage_dict[tech.id]
        except:
            self.storage_dict[tech.id]=0
        return result

    def to_move(self,tech,count):
        result=False
        try:
            count=int(count)
        except:
            count=0

        try:
            self.storage_dict[tech.id]=self.storage_dict[tech.id]+int(count)

        except:
            self.storage_dict[tech.id]=int(count)

        result=self.storage_dict[tech.id]

        if result<0:
            result=False
            self.storage_dict[tech.id]=self.storage_dict[tech.id]-int(count)
        return result

    def to_out(self,subject,tech,count):
        result=0
        try:
            count=int(count)
        except:
            count=0

        try:
            result=self.storage_dict[tech.id]
        except:
            self.storage_dict[tech.id]=0

        if result>0 and result>=count:
            self.to_move(tech,-1*count)
            subject.to_move(tech,count)
            result=count
        else:
            result=False
        return result

p1=Printer("HP","C100")
print(p1)
p1.to_print()

x1=Xerox("Xerox","x100")
print(x1)
x1.to_xerox()

s1=Scaner("Cannon","sc200")
print(s1)
s1.to_scan()

s=Storage("Главный склад")
print(s.to_get(p1))
print(s.to_move(p1,3))
print(s.to_move(x1,0))
print(s.to_move(s1,10))
print(s.to_move(p1,0))
print(s.to_move(p1,"234"))
print(s.to_move(p1,-4))
print(s.my_list())

o=Storage("Коморка")
print(o.to_move(s1,2))
print(o.my_list())

print(s)
print(o)
print(f"Переместили {p1} ", s.to_out(o,p1,1))
print(s)
print(o)
class Stationery:
    title=""

    def draw(self):
        print ("Запуск отрисовки")


class Pen(Stationery):
    title="Ручка"

    def draw(self):
        print ("Тонко пишет",self.title)

class Pencil(Stationery):
    title="Карандаш"

    def draw(self):
        print ("Царапает",self.title)

class Handle(Stationery):
    title="Маркер"

    def draw(self):
        print ("Жирно мажет",self.title)



p=Pen()
p.draw()

c=Pencil()
c.draw()

h=Handle()
h.draw()
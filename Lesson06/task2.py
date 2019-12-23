class Road:
    def __init__(self,lenght,width):
        self._lenght=lenght
        self._width=width


    def weight(self,height=0):
        #print (self.lenght,self.width)
        return int(self._lenght)*int(self._width)*25*int(height)/1000

r=Road(5000,20)
print(f"{r.weight(5)} т.")
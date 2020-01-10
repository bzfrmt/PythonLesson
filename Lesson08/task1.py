class Data:
    data=""
    day=0
    month=0
    yaer=0

    def __init__(self,data):
        self.data=data

    @staticmethod
    def validatedata(day,month,year):
        daydict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        vday=0
        if year%4==0 and month==2:
            vday=1
        if year<1900 or year>2100:
            print ("Год не соотвествует критериям")
        elif month<0 or month>12:
            print ("Месяц не соотвествует критериям")
        elif day<0 or day>daydict[month]+vday:
            print ("День не соотвествует критериям")
        else:
            print ("Дата соотвествует требованиям")

    @classmethod
    def getintday(cls,data):
        return int(data.split("-")[0])

    @classmethod
    def getintmonth(cls,data):
        return int(data.split("-")[1])

    @classmethod
    def getintyear(cls,data):
        return int(data.split("-")[2])



d=Data("29-02-2000")
d.day=Data.getintday(d.data)
d.month=Data.getintmonth(d.data)
d.year=Data.getintyear(d.data)
Data.validatedata(d.day,d.month,d.year)
print (d.day,d.month,d.year)
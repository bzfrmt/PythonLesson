class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
num=""
numlist=[]
while num.upper()!="STOP":
    try:
        num=input("Введите число: ")
        #nnum=int(num)

        if not num.isdigit():
            raise OwnError("Не число!")
    #except ValueError:
        #pass
        #print("Вы ввели не число")
        #raise OwnError("Не число!")
    except OwnError as err:
        print(err)
    else:
        numlist.append(int(num))


print (numlist)
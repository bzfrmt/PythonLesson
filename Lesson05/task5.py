import random
numbers=[random.randint(0,100) for i in range(100)]

print (" ".join(map(str, numbers)))
if len(numbers)>0:
    fw = open("task5.txt", "w",encoding="cp1251")
    print(" ".join(map(str, numbers)),file=fw)
    fw.close()


try:
    fw = open("task5.txt", "r",encoding="cp1251")
    resultnumbers=fw.read().split()
    fw.close()
except:
    print("Ошибка чтения файла")

else:
    #summa=0
    #for number in resultnumbers:
    #    summa=summa+int(number)
    #print(summa)

    print("Сумма: ",sum(map(int,resultnumbers)))
numbers_str="0"
summa=0
while numbers_str:
    if summa>0:
        print ("Сумма: ",summa)
    numbers_str=input("Введите строку чисел, для выхода введите пустую строку или Q: ")
    numbers_list=numbers_str.split()

    for number in numbers_list:
        try:
            summa=summa+int(number)
        except:
            print ("Ошибка в числе: ",number)
            if number.upper()=="Q":
                numbers_str=False
                print("Выход")
                break

print ("Сумма: ",summa)
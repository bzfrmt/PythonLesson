def funct (a,b):
    result=0
    try:
        result=a/b
    except ZeroDivisionError:
        print('Ошибка. Деление на ноль')

    return result




try:
    first=int(input('Введите первое число: '))
    second=int(input('Введите второе число: '))

except:
    print('Не корректное число')

print ("%.3f" % funct(first,second))
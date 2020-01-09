class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt



try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))

    if b==0:
        raise OwnError("Деление на ноль не допустимо!")
except ValueError:
    print("Вы ввели не число")

except OwnError as err:
    print(err)
else:
    print("Отношение: ",a/b)
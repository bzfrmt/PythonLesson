maxage=100
years=0

print("Привет, я Вещая кукушка")

name=input("Представьтесь: ")

print (f"Привет {name}")

age=input("Сколько тебе годков?: ")

age=int(age)
years=maxage-age
if years >0 :
    print(f"{name} осталось, считай:")
    while years > 0 :
        years=years-1
        print ("Ку-Ку")
elif years==0:
    print("Странно что ты еще здесь! Собирай чемодан")
else:
    print(f"{name}, ты живой не погодам!")
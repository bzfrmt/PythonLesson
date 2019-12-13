def user (**kwargs):
    #print(str(kwargs))
    result="Пользователь:"
    for k,v in kwargs.items():
        result=result + " " + str(k) + ":" + str(v)
    return result
print (user(name='Вася',year=1980,city='Msk',email='vasa@mail.ru',phone='790345344'))


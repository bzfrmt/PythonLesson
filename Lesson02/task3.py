month=int(input("Введите порядковый номер месяца в году от 1 до 12: "))
month_list=["","зима","зима","весна","весна","весна","лето","лето","лето","осень","осень","осень","зима"]
month_dict={1:"зима",2:"зима",3:"весна",4:"весна",5:"весна",6:"лето",7:"лето",8:"лето",9:"осень",10:"осень",11:"осень",12:"зима"}

if month>0 and  month<13:
    print (month_list[month])
    print (month_dict[month])

else:
    print("Ввели не верное число")
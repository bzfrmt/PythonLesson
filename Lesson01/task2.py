sec=int(input("Введите время в секундах: "))
if sec<0:
    print ("Введите корректное значение")
else:
    hours=sec//3600
    #print (hours)
    minutes=(sec-hours*3600)//60
    #print (minutes)
    seconds=(sec-hours*3600-minutes*60)
    #print (seconds)
    print(f"%02i:%02i:%02i" % (hours, minutes, seconds))

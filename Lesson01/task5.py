inmoney=int(input("Укажите выручку фирмы: "))
outmoney=int(input("Укжите издержки фирмы: "))

money=inmoney-outmoney

if money> 0:
    print(f'Прибыль составила {money}')
    print('Рентабельность','%.2f' % (money/inmoney*100),'%')
    peoples=int(input("Укажите колличество сотрудников фирмы: "))
    print ('Прибыль на каждого сотрудника составила: ',money//peoples)
elif money<0:
    print('Убыток составил:',money)
else:
    print('Сработали в ноль')

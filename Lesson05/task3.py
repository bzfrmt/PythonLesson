summa=0
members=0
with open("task3.txt","r",encoding="cp1251") as f:
    for line in f:
        member=line.split()
        summa=summa+int(member[1])
        members=members+1
        if int(member[1]) <20000:
            print(member[0])

if members>0:
    print("Средний оклад составляет: ",summa/members)
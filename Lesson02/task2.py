print ("Давайте заполним спиок")
print ("Чтобы прервать ввод введите пустую строку")
mylist=[]
valitem="0"
i=0
while len(valitem)>0:
    i=i+1
    valitem=input(f"ведите значение {i}-го эелемента: ")
    if  len(valitem)>0:
        mylist.append(valitem)

print(mylist)
if len(mylist) > 1:
    for i in range(len(mylist)//2):
        mylist[i*2],mylist[i*2+1] = mylist[i*2+1],mylist[i*2]

print(mylist)
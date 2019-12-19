str="start"

f = open("task1.txt", "w")
while len(str)>0 :

    str=input("Введите строку: ")
    print (str)
    f.write(str + "\n")

f.close()
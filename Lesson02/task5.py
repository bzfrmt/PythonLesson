my_list = [7, 5, 3, 3, 2]

print(my_list)

newpos=int(input("Введите новое значение: "))

maxpos=max(my_list)
#print(maxpos)

minpos=min(my_list)

#print(minpos)

if maxpos<newpos:
    my_list.insert(0,newpos)

elif minpos>=newpos:
    my_list.append(newpos)

else:

    for i in range(len(my_list)):
        #print(my_list[i])
        if my_list[i]<newpos:
            #print (f"Позиция :{i}")
            break
    my_list.insert(i,newpos)



    #print(i)
print(my_list)
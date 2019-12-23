import re
result_dict={}
with open("task6.txt","r",encoding="cp1251") as f:
    for line in f:
        summa=0
        #print(line)
        obj=re.search("(\w+)\s*\:\s*(?:(\d+)\(\w+\)|\-)\s+(?:(\d+)\(\w+\)|\-)\s+(?:(\d+)\(\w+\)|\-)", line)
        if obj[1]:
            #print (obj[1],obj[2],obj[3],obj[4])
            if obj[2]:
                summa=summa+int(obj[2])
            if obj[3]:
                summa=summa+int(obj[3])
            if obj[4]:
                summa=summa+int(obj[4])
            result_dict[obj[1]]=summa

print(result_dict)


digitword={1:"один",2:"два",3:"три",4:"четыре"}
resultstring=""
with open("task4.txt","r",encoding="cp1251") as f:
    for line in f:
        member=line.split("-")
        #
        #fw = open("task4_result.txt", "a",encoding="cp1251")
        #print(digitword[int(member[1])],"-",int(member[1]),file=fw)
        #fw.close()
        resultstring=resultstring+str(digitword[int(member[1])])+"-"+str(int(member[1]))+"\n"

if len(resultstring)>0:
    fw = open("task4_result.txt", "w",encoding="cp1251")
    print(resultstring,file=fw)
    fw.close()
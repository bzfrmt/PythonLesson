class Matrix:
    matrixlist=[]
    countrows=0
    countstr=0

    def __init__(self,matrixlist):
        if type(matrixlist)==list:
            self.matrixlist=matrixlist
            print (matrixlist)
            self.countrows=max([len(el) for el in matrixlist])
            #print(self.countrows)
            self.countstr=len(matrixlist)
            #print(self.countstr)
        else:
            print("Ошибка ввода Матрицы")

    def __str__(self):
        result=""
        for i in self.matrixlist:
            result +=" ".join(map(str,i))
            result +="\n"
        return result

    def __add__(self, other):
        resultlist=[]
        for i in range(max([self.countstr,other.countstr])):
            resultstr=[]
            #print (i)
            for j in range(max([self.countrows,other.countrows])):
                #print (i,j)
                #Есть ли более лаконичный способ проверить сществование переменной или элемента списка?
                #Может есть в python что-то наподобие функции isset() ?
                try:
                    a=self.matrixlist[i][j]
                except:
                    a=0
                b=0
                try:
                    b=other.matrixlist[i][j]
                except:
                    b=0
                resultstr.append(a+b)
            resultlist.append(resultstr)
        return Matrix(resultlist)


m1=Matrix([[1,2],[2,1,3,1],[3,1,2]])
print(m1)
m2=Matrix([[1,2,3],[2,1,3],[3,1,2],[3,1]])
print(m2)

print(m1+m2)
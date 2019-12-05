digit=int(input("Введите число: "))
i=0
maxdigit=0
if digit>0:
    digitstr=str(digit)
    while i<len(digitstr):
        #print(digitstr[i])
        if maxdigit<int(digitstr[i]):
            maxdigit=int(digitstr[i])
        i=i+1
    print (maxdigit)
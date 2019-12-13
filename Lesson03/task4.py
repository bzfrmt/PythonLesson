x=2
y=-3

def my_func(x,y):
    #1 способ
    result=x**y
    #2 способ
    result=x
    for i in range(1,abs(y)):
        result=result*x
    return 1/result


print(my_func(x,y))
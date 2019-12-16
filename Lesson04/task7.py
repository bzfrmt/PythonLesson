def fibo_gen():
    for el in range(1,16):
        for i in range(1,el):
            el=el*i
        yield el

for el in fibo_gen():
    print(el)
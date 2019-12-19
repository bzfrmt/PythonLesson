#бесконечный цикл count
from itertools import count

for el in count(1):
    print (el)
    if el > 100:
        break

#бесконечный перебор
from itertools import cycle
my_list=[1,2,5,3,4,8,10,11,9,14,15,7,16,2,20]

for el in cycle(my_list):
    if el > 10:
        break
    print(el)
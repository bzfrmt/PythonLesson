#1
print([number for number in range(20,240) if (number%20==0 or number%21==0)] )
#2
print(sorted([number for number in range(20,240,20)]+[number for number in range(21,240,21)]))
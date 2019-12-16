my_list=[1,2,5,3,4,8,10,11,9,14,15,7,16,2,20]


new_list = [el for el in my_list if my_list.count(el)==1]
print(new_list)

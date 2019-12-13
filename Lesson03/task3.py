
def my_func(*args):
    mylist=sorted(args)
    return int(mylist[-1])+int(mylist[-2])



print (my_func(6,5,4))
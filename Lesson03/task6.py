def int_func(word=''):
    return str(word[0].upper())+str(word[1:])

#print (int_func("ssdf"))

words_string=input("Введите строку: ")
words=[]

if len(words_string)>0:
    for word in words_string.split():
        #print (int_func(word))
        words.append(int_func(word))
    print (' '.join(words))


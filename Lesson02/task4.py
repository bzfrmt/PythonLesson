wordstring=input("Введите строку: ")

words=wordstring.split(" ")

for word in words:
    print(word[0:10])
f = open("task2.txt", "r")
content = f.readlines()
print ("Строк в файле: ", len(content))
for i in range(len(content)):
    print(f"строка {i+1} содержит {len(content[i].split())} слов")
f.close()
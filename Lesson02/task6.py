products=[]
pprops=["название", "цена", "количество", "eд"]

#products=[(1, {'название': 'ыфвафы', 'цена': 'ыфва', 'количество': 'фыва', 'eд': 'шт'}), (2, {'название': 'ываф', 'цена': 'ыфва', 'количество': 'фыва', 'eд': 'шт'})]

product_line=tuple()
count_product=int(input("Ведите количество позиций товара: "))

for i in range(count_product):
    product={}
    for pprop in pprops:
        product[pprop]=input(f"Введите {pprop} товара № {i+1}: ")
    #print(product)
    products.append(tuple((i+1,product)))

print("Товары:")
print (products)

report={}
for pprop in pprops:
    propline=[]
    for p in products:
        #print (pprop,p[1][pprop])
        if p[1][pprop] not in  propline:
            propline.append(p[1][pprop])
    report[pprop]=propline

print("Онолитега:")
print(report)
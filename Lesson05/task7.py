import json
import re
result_list=[]
firm_dict={}
average_dict={}
average_profit=0
count_profit=0
with open("task7.txt","r",encoding="cp1251") as f:
    for line in f:
        profit=0
        firma=obj=re.search("(\w+)\s+\w+\s+(\d+)\s+(\d+)", line)
        profit=int(firma[2])-int(firma[3])
        print(firma[1],profit)
        firm_dict[firma[1]]=profit
        if profit>=0:
            average_profit=average_profit+profit
            count_profit=count_profit+1

    if count_profit>0:
         average_profit=average_profit/count_profit
    #print(average_profit,count_profit)
    average_dict["average_profit"]=average_profit

#print(firm_dict)
#print(average_dict)
result_list.append(firm_dict)
result_list.append(average_dict)
print(json.dumps(result_list))

with open("task7.json", "w", encoding="cp1251") as f:
    json.dump(result_list, f)
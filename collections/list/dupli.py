# create a new list where no duplicate elements are there
lst=[10,10,30,30,40,40,50,50,60,70,'bigdata','bigdata']
list=[]
for i in lst:
    if i not in list:
        list.append(i)
print(list)
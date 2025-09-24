# find  the count of the object with same character as the starting and ending eg: ded
lst=['abc','ded','fgh','hih','jkl','mno','pqp','123','454','5','4']
lst1=[]
j=0
for i in lst:
    if i[0]==i[-1] and len(i)>1:
        lst1.append(i)
print(lst1)
print(len(lst1))

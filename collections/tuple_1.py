# change the value in a tuple
tu=(10,15,20,25,30,35,40,45,100)
# update the value 35 into 75
lst=list(tu)
print(lst)
lst[5]=75
print(lst)
tu=tuple(lst)
print(tu)
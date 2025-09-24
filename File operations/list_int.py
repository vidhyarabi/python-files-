lst=[1,3,5,4,3,5,6,7,8,9,7,5,4,6,9,10,12,10,9,8,5,8,9,10]
# new list=[1,5,3,9,4,12,5]
lst1=[]
for i in range(0,(len(lst)-1)):
    if ((i-1)<i<(i+1)):
        lst1+=lst[i]
print(lst1)
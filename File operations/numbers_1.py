f=open('numbers1','r')
lst=[]
for i in f:
    lst.append(int(i.rstrip('\n')))
print(lst)
lst1=[]
lst2=[]
for i in lst:
    if i%2==0:
        lst1.append(i)
    else:
        lst2.append(i)
print(sum(lst))
print(lst1)
print(sum(lst1))
print(lst2)
print(sum(lst2))
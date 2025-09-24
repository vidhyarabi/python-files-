lst=[6,8,2,8,3,4,10,15,22,6,99,34,3,1]
flag=0
lst.sort()
print(lst)
num=int(input('Enter the number:'))
low=0
upper=len(lst)-1
while low<=upper:
    mid=(low+upper)//2
    if num<lst[mid]:
        upper=mid-1
    elif num>lst[mid]:
        low=mid+1
    elif num==lst[mid]:
        print('found')
        break

else:
    print('not found')
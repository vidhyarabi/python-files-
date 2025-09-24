# binary search algorithm

lst=[1,10,3,7,9,2,4,6,15,12,11,13]
lst.sort()
print(lst)
flag=0
low=0
upper=len(lst)-1
num=int(input('Enter the number: '))
while (low<=upper):
    mid=(low+upper)//2
    if num>lst[mid]:
        low=mid+1
    elif num<lst[mid]:
        upper=mid-1
    elif num==lst[mid]:
        print('found')
        break

else:
    print('not found')

#      or
# line 16
#     elif num==lst[mid]:
#          flag=1
#           break
# if flag==0:
#    print('not found')
# else:
#      print('found')

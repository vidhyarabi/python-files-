# 1 to 50 even : square ,  odd : cube print

lst=[i**2 if i%2==0 else i**3 for i in range(1,51)]
print(lst)

lst1=[(i,i**2) if i%2==0 else (i,i**3) for i in range(1,51)]
print(lst1)

#  1 to 20 range even : type even odd:  type odd

lst2=[(i,"even") if i%2==0 else (i,'odd') for i in range(1,21)]
print(lst2)
# 1 to 10 range odd numbers square
list=[]
for i in range(1,11):
    if i%2==1:
        list.append(i**2)
print(list)
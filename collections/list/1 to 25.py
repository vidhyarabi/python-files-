# add 1 to 25 divisible by 5
list=[]
for i in range(1,26):
    if i%5==0:
        list.append(i)
print(list)
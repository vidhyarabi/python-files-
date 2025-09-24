# count length of the words
sentence='this is a sample sentence'
sen=sentence.split(' ')
lst1=[len(i) for i in sen ]
print(lst1)

# reverse the given words in the list eg: apple - elppa

words=['apple','banana','cherry']
lst2=[i[::-1] for i in words]
print(lst2)
# lst4=[i.__reversed__() for i in words]


# generate list of tuple containing two numbers whoes sum is even
# output=[(1,1),(1,3),(1,5)....]
lst3=[(i,j) for i in range(1,10) for j in range(1,10) if (i+j)%2==0]
print(lst3)



# capitalize the first letters of the words in the list words

lst4=[i.capitalize() for i in words ]
print(lst4)

#  how many times each number is repeated

lst5=[1,2,2,3,4,4,4,5]
lst6={num:lst5.count(num) for num in lst5}
print(lst6)
#  or we can convert into set then we will get the same output

lst7={num:lst5.count(num) for num in set(lst5)}
print(lst7)
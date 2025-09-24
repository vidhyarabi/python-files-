lst=[[101,'vinay','k',31,'bigdata',1000],
     [102,'anu','l',31,'python',1500],
     [103,'vid','p',32,'testing',3000],
     [104,'vig','b',28,'bigdata',25000]]
# age above 30
#for i in lst:
 #   if i[3]>30:
  #      print(i)

# age equal to 31 fname,lname,age,prof

#for i in lst:
 #   if i[3]==31:
  #      print(i[1:5])


# big data prof people fname,lname,age

#for i in lst:
 #   if i[4]=='bigdata':
  #      print(i[1:4])

# python prof  print fname,age,salary
#for i in lst:
 #   if i[4]=='python':
  #      print(i[1::2])

# bigdata prof and age above 30 - fname,lname,age
for i in lst:
    if i[4]=='bigdata' and i[3]>30:
        print(i[1:4])

# calculate total salary

salary=0
for i in lst:
    salary+=i[5]
print(salary)

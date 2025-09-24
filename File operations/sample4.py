f=open('C:/Users/vidhy/OneDrive/Documents/sample4.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    # print(data)
    age=data[3]
#     if age=='21':
#         print(data)

#  age above 22 - fname,lname,age,phno
#     if age>'22':
#         print(data[1:5])

# age below 23 - fname,lname,age
#     if age<'23':
#         print(data[1:4])

#  chennai work - fname,lname,age,ph
#     if data[5]=='Chennai':
#         print(data[1:5])

# chennai work and age above 23 - fname,age,loc
    if data[5]=='Chennai' and data[3]>'23':
        print(data[1::2])
# age abouve 50 - fname,lname,age,prof
f=open('C:/Users/vidhy/OneDrive/Documents/customer1.txt','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    age=data[3]
    loc=data[-1]
    prof=data[4]
    # if age>'50':
    #     print(data[1:5])


# 2.age above 25 fname,lname,age,prof
#     if age>'25':
#         print(data[1:5])

#3. age between 25 to 40 fname,age,loc
    # if '25'<age<'40':
    #     print(data[1::2])


# 4.india work fname,lname,age,prof

    # if loc=='india':
    #     print(data[1:5])
#5. india work and age above 50 fname,lname,age

    # if loc=='india' and age>'50':
    #     print(data[1:4])
# 6. doctor prof work ,fname,lname,age)
#     if prof=='Doctor':
#         print(data[1:4])

# 7. UK and prof doctor fname,lname,age
#     if loc=='uk' and prof=='Doctor':
#         print(data[1:4])

# 8. Pilot prof work faname,lname,age
#     if prof=='Pilot':
#         print(data[1:4])

# 9. india and prof doctor fname,lname,age
#     if loc=='india' and prof=='Doctor':
#         print(data[1:4])
# 10. Each profession count
#     if prof not in dic:
#         dic[prof]=1
#     else:
#         dic[prof]+=1
# print(dic)

# 11. Each location count

    if loc not in dic:
        dic[loc]=1
    else:
        dic[loc]+=1
for k,v in dic.items():
    print(k,':',v)



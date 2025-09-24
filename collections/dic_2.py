dic={'id':101,'fname':'vinay','lname':'k','age':28,'prof':'bigdata','salary':1000}
print(dic)
print(dic['prof'])
# print complete key and value separately
for i in dic:
    print(i)
    print(i,dic[i])
    print(i,':',dic[i])

# dictionary is mutable
dic['prof']='python'
dic['age']=30
dic['salary']+=500
print(dic)
dic['location']='ernakulam'
dic['marks']=75
print(dic)
del dic['lname']
del dic['marks']
print(dic)
print('lname' in dic)
print('prof' in dic)
print('sub' not in dic)
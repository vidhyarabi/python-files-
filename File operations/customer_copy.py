# read the customer file
# count of the workers in each profession
# result==> copy
f=open('C:/Users/vidhy/OneDrive/Documents/customer1.txt','r')
f1=open('customer_copy1','w')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    prof=data[4]
    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
for k,v in dic.items():
    res=k+':'+str(v)+'\n'
    f1.write(res)
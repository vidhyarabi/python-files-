# find the maximum temp in a district

f=open('C:/Users/vidhy/OneDrive/Documents/temper.unknown','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    district=data[0]
    temp=data[1]
    if district not in dic:
        dic[district]=temp
    else:
        old=dic[district]
        if temp>old:
            dic[district]=temp
for k,v in dic.items():
    print(k,':',v)
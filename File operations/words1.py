# f=open('words','r')
# sentence=''
# for i in f:
#     sentence+=(i.rstrip('\n'))
# print(sentence)
# lst=sentence.split()
# print(lst)
# dic={}
# for i in lst:
#     if i not in dic:
#         dic[i]=1
#     else:
#         dic[i]+=1
# print(dic)

f=open('words','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(' ')

    for i in data:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
print(dic)
for i in dic:
    print(i,': ',dic[i])
print('stop it and go to the next one')
for k,v in dic.items():
    print(k,':',v)
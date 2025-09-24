# wordcount - number of repetition of a word
sentence='cat rat bus cat rat bus mango mango car cat rat cat'
lst=sentence.split(' ')
print(lst)
dic={}
for i in lst:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)


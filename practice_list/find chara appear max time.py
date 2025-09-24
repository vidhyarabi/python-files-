# write a program to find the charcter that appears the most number of times in the string
string=input('Enter the sentence: ')
dic={}
lst=string.split()
for i in string:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
max_char=''
max_count=0
for i in dic:
    if dic[i]>max_count:
        max_char=i
        max_count=dic[i]
print('the most repeated letter is',max_char,'with the count of',max_count)
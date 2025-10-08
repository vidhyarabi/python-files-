# write a program to find the character that appears the most number of times in a string .
# Example: 'banana' -> 'a' appears 3 times.

string=input('Enter the string :')
dic={}
for i in string:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
count=0
character=''
for i in dic:
    if dic[i]>count:
        count=dic[i]
        character=i
print(character,'appears',count,'times')
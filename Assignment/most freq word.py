# Write a program to find the word that occurs the most in a sentence
# Example: "this is a test and the test" -> 'test' appear twice
string=input('Enter the string: ')
lst=string.split(' ')
dic={}
for i in lst:
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
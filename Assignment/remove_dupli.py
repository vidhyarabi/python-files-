# Write a program that removes all duplicate characters and returns the string with only the first occurrence kept
# Example: 'programming' -> 'progamin'
string=input('Enter the number: ')
dic={}
for i in string:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    print(i,end='')
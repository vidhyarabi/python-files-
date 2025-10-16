# Write a program to check whether a string has duplicate character or not.
# example : 'unique' --> output : yes (since 'u' appears more than once)
string=input('Enter the string: ')
dic={}
for i in string:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    if dic[i]>1:
        print("yes (since ", i ,' appears more than once)')
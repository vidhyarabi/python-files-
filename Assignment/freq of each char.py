# Write a program to count and display the frequency of each character in the string .
# Example: 'apple' --> {'a':1,'p':2,'l':1,'e':1}
string=input('Enter the string: ')
dic={}
for i in string:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    print(k,':',v,end=' , ')
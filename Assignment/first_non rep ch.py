# Write the program to find the first non-repeating character in a string
# Example : 'swiss' -> Output:'w'
string=input('Enter the string: ')
dic={}
for i in string:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    if dic[i]==1:
        print(i)
        break
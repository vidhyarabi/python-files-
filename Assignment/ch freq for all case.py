# Write a program to count character frequencies without considering case ( i.e., 'A' and 'a' are the same).
# Example: 'APPLEapple' -> 'a':2,'p':4,'l':2,'e':2
string=input('Enter the string: ')
dic={}
for i in string:
    ch=i.lower()
    if ch not in dic:
        dic[ch]=1
    else:
        dic[ch]+=1

for k,v in dic.items():
    print(k,':',v,end=" , ")
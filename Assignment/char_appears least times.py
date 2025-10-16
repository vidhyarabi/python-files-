# write a program to find the character that appears the least number of times (excluding spaces);
# example 'mississippi' -> 'm' appears once
string=input('string: ')
dic={}
first=True
for ch in string:
    if ch!=" ":
        if ch not in dic:
            dic[ch]=1
        else:
            dic[ch]+=1
for ch in dic:
    if first:
        min_count=dic[ch]
        first=False
    elif dic[ch]< min_count:
        min_count = dic[ch]
for ch in dic:
    if dic[ch]==min_count:
        print('least frequent character:',ch)
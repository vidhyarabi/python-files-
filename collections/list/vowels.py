# find the vowels count in a string
string='luminartechnolab'
count=0
vowels=['a','e','i','o','u','A','E','I','O','U'] # or vowels='aeiouAEIOU'
for i in string:
    if i in vowels:
        count+=1
print(count)

# using list  and finding its length

string1='luminartechnolab'
vowels='aeiouAEIOU'
lst=[]
for i in string1:
    if i in vowels:
        lst.append(i)
print(lst)
print(len(lst))
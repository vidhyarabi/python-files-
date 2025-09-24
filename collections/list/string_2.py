# count number of consonants
string='luminartechnolab'
vowels='aeiouAEIOU'
list=[]
for i in string:
    if i not in vowels:
        list.append(i)
print(list)
print(len(list))
    
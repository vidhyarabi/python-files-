# find the consonant count in a string

string='luminartechnolab'
vowels='aeiouAEIOU'
lst=len([i for i in string if i not in vowels])
print(lst)
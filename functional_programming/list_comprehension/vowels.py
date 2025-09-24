# find the count of vowels in the given string

string='luminartachnolab'
vowels='aeiouAEIOU'
lst1=len([i for i in string if i in vowels ])
print(lst1)
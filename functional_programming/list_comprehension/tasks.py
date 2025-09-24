# find all of the numbers from 1 to 1000 that are divisible by 7

lst=[i for i in range(1,1001) if i%7==0]
print(lst)

# find all of the numbers from 1 to 1000 that have 3 in them

lst1=[i for i in range(1,1001) if '3' in str(i)]
print(lst1)

# count number of spaces in a string
string='practice list comprehension problems to drill your head'
lst2=len([i for i in string if i==' ' ])
print(lst2)

# count number of vowels in a string

vowels='aeiouAEIOU'
lst3=len([i for i in string if i in vowels])
print(lst3)

# get only numbers in a sentence
sentence='in 1984 there were 13 instance of a protest with over 1000 people attending'
sen=sentence.split(' ')
print(sen)
num=[1,2,3,4,5,6,7,8,9]
lst4=[i for i in sen if not i.isalpha()]
print(lst4)
# lst4=[i for i in sen if i.isnumeric()/ i.isdigit()]

# find all of the words in a string that are less than 4 letters
str=string.split(' ')
lst5=[i for i in str if len(i)<5]
print(lst5)

lst6=[i for i in sen if i in num]
print(lst6)
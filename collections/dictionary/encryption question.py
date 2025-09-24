num=int(input('Enter the number: '))
letter=input('Enter the letter: ').upper()
lst=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
index=lst.index(letter)
for i in lst:
    if letter.lower() in lst:
        print(lst[index+num].lower())
        break
    elif letter.upper() in lst:
        print(lst[index+num].upper())
        break
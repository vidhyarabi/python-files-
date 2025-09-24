# read lower and upper limit and print the odd numbers in between them
lower=int(input('Enter the number: '))
upper=int(input('Enter the number: '))
while lower<=upper:
    if lower%2==1:
        print(lower)
    lower+=1
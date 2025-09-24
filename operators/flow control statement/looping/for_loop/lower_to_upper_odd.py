lower=int(input('Enter a number: '))
upper=int(input('Enter a number: '))
for i in range(lower,upper+1):
    if i%2!=0:
        print(i)
  # lower to upper limit and print the numbers divisible by 5
lower=int(input('Enter lower limit: '))
upper=int(input('enter upper limit: '))
while lower<=upper:
    if lower%5==0:
        print(lower)
    lower+=1
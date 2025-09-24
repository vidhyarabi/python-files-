# lower , upper , sum of odd numbers in between them
lower=int(input('Enter lower limit: '))
upper=int(input('enter upper limit: '))
sum=0
while lower<=upper:
    if lower%2==1:
        sum+=lower
    lower+=1
print(sum)
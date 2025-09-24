# lower,upper , lower to upper even sum and odd sum
lower=int(input('Enter lower limit: '))
upper=int(input('enter upper limit: '))
sum1=0
sum2=0
while lower<=upper:
    if lower%2==0:
        sum1+=lower
    else:
        sum2+=lower
    lower+=1
print('sum of even numbers:',sum1)
print('sum of odd numbers',sum2)
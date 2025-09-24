# lower
# upper
# lower  to upper even_numbers sum
lower=int(input('Enter lower number: '))
upper=int(input('Enter upper number: '))
sum=0
while lower<=upper:
    if lower%2==0:
        sum+=lower
    lower+=1
print(sum)
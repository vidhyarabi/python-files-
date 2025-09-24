lower=int(input('Enter the number: '))
upper=int(input('Enter the number: '))
sum=0
for i in range(lower,upper+1):
    if i%2==0:
        sum+=i
print(sum)
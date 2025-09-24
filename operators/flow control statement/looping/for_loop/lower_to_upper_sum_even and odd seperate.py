lower=int(input('Enter a number: '))
upper=int(input('Enter a number: '))
even_sum=0
odd_sum=0
for i in range(lower,upper+1):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print('even sum=',even_sum)
print('odd sum=',odd_sum)
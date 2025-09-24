# factorial of a number eg: 4! = 1*2*3*4
num=int(input('Enter a number: '))
i=1
fact=1
while i<=num:
    fact*=i
    i+=1
print(fact)
# check given number is prime or not
num=int(input('Enter the number: '))
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
if flag==1:
    print('Not a prime')
elif num==1:
    print('neither prime nor consonant')
else:
    print('prime')
# largest among 3 numbers
num1=int(input('Enter number one: '))
num2=int(input('enter number 2: '))
num3=int(input('Enter number3: '))
if (num1>num2)&(num1>num3):
    print('num1 is greatest')
elif (num2>num1)&(num2>num3):
    print('num2 is greatest')
else:
    print('num3 is largest')
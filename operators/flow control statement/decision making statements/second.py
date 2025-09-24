#find the second largest number
num1=int(input('enter number1: '))
num2=int(input('Enter number2: '))
num3=int(input('Enter number3: '))
if num2<num1<num3 or num3<num1<num2 :
    print(num1)
elif num1<num2<num3 or num3<num2<num1:
    print(num2)
else:
    print(num3)
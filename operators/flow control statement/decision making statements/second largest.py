num1=int(input('enter no.1: '))
num2=int(input('enter number 2: '))
num3=int(input('enter number3: '))
if num1>num2 and num1>num3:
    if num2>num3:
        print(num2,'is the second largest')
    else:
        print(num3,'is the second largest')
elif num2>num1 and num2>num3:
    if num1>num3:
        print(num1,'is the second largest')
    else:
        print(num3,'is the second largest')
elif num3>num1 and num3>num2:
    if num1>num2:
        print(num1,'is the second largest')
    else:
        print(num2,'is the second largest')
else:
    print('Equal') # without else part also this problem will run
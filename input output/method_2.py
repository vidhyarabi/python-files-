#swapping of 2 numbers without a third variable


num1=10
num2=20
print('Before swapping')
print('Number1 is',num1)
print('Number2 is',num2)

num1=num1+num2 # num1=10+20=30
num2=num1-num2 # num2=30-20=10
num1=num1-num2
print('After swapping')
print('number1 is',num1)
print('number2 is',num2)
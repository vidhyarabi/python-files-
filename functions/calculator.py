# create a simple calculator
# 1 for addition
# 2 for substraction
# 3 for mult
# 4 for div
# read num1 and num2 and read a choice from read
# and if the choice is the above number then do that operation
def add(num1,num2):
    res=num1+num2
    return res
def sub(num1,num2):
    res=num1-num2
    return res
def mult(num1,num2):
    res=num1*num2
    return res
def div(num1,num2):
    res=num1/num2
    return res
print("1.addition\n"
      "2.substraction\n"
      "3.multiplication\n"
      "4.division")
num1=int(input('Enter num1: '))
num2=int(input('Enter num2: '))
choice=int(input('your choice: '))
if choice==1:
    print(add(num1,num2))
elif choice==2:
    print(sub(num1,num2))
elif choice==3:
    print(mult(num1,num2))
elif choice==4:
    print(div(num1,num2))
else:
    print('choice not allowed')
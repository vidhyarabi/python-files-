# reverse a number
# read a number eg: num=153 ans: 351
from unicodedata import digit

num=int(input('enter a number: '))
res=0
while num!=0:
    digit=num%10
    res=((res*10)+digit)
    num//=10
print(res)
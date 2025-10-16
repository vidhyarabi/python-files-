# print('hello')
# num1=10
# num2=20
# print('num1=',num1)
# print('num2=',num2)
# temp=num1
# num1=num2
# num2=temp
# print('num1=',num1)
# print('num2=',num2)
# num1=10
# num2=20
# num1=num1+num2
# num2=num1-num2
# num1=num1-num2
# print(num1)
# print(num2)
# num1=10
# num2=20
# num1,num2=num2,num1
# print(num1)
# print(num2)
# lower=int(input('lower limit: '))
# upper=int(input('upper limit: '))
# sum=0
# while lower<=upper:
#     if lower%2==0:
#         sum+=lower
#     lower+=1
# print(sum)
# num=int(input('enter the number: '))
# res=0
# while num!=0:
#     digit=num%10
#     res=(res*10)+digit
#     num//=10
# print(res)
# num=int(input('enter: '))
# count=0
# while num!=0:
#     num//=10
#     count+=1
# print(count)
# for i in range(0,6):
#     for j in range(i+1):
#         print(j*i,end=' ')
#     print()
# for i in 'luminar technolab':
#     print(i)
# def add():
#     num1=int(input('enter no1'))
#     num2=int(input('enter no2'))
#     sum=num1+num2
#     print(sum)
#
# add()
# add()
# lower=int(input('lower:'))
# upper=int(input('upper:'))
# num=0
# for i in range(lower,upper+1):
#     if i>1:
#         flag=0
#         for j in range(2,i):
#             if i%j==0:
#                 flag=1
#                 break
#         if flag==1:
#             pass
#         else:
#             print(i)
#             num+=1
# print(num)

# lower=int(input('lower:'))
# upper=int(input('upper:'))
# num=0
# for i in range(lower,upper+1):
#     if i>1:
#         flag=0
#         for j in range(2,i):
#             if i%j==0:
#                 flag=1
#                 break
#         if flag==0:
#             num+=1
# print(num)

# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     return fact
# data=factorial(3)
# print(data)
# print('1. add'
#       '2.sub '
#       '3.mul ')
from operators.demo import *
# def fib(num):
#     a,b=0,1
#     for i in range(num):
#         print(a,end=' ')
#         a,b=b,a+b
# numbers=int(input('enter the numbers'))
# fib(numbers)
# def fib(num):
#     a,b=0,1
#     for i in range(num):
#         print(a,end=' ')
#         a,b=b,a+b
# number=int(input('enter the number: '))
# fib(number)
# def vowel_count(str):
#     count=0
#     vowel='aeiouAEIOU'
#     for i in str:
#         if i in vowel:
#             count+=1
#     return count
# data=vowel_count('vidhya')
# print(data)
# num=int(input('enter the number: '))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)
num=int(input('enter: '))
# count=0
# while num!=0:
#     num//=10
#     count+=1
# print(count)
res=0
while num!=0:
    digit=num%10
    res=(res*10)+digit
    num//=10
print(res)

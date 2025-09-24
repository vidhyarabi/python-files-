def fib(num):
    a,b=0,1
    for i in range(num):
        print(a,end=' ')
        a,b=b,a+b
numbers=int(input('enter the number: '))
fib(numbers)
def sum():
    lower=int(input('Enter the number: '))
    upper=int(input('enter the number: '))
    res=0
    for i in range(lower,upper+1):
        if i%2==0:
            res+=i
    print(res)
sum()
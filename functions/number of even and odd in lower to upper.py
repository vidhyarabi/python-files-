def number():
    lower=int(input('Enter the number: '))
    upper=int(input('Enter the number: '))
    count_1=0
    count_2=0
    for i in range(lower,upper+1):
        if i%2==0:
            count_1+=1
        else:
            count_2+=1
    print('even count=',count_1)
    print('odd count=',count_2)
number()
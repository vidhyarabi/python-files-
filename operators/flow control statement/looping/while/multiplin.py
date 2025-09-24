# multiplication table of a given number - read a num from the user and get the multiplication table of that num
num=int(input('Enter a number: '))
i=1
while i<=10:
    mult=num*i
    print(i,'*',num,'=',mult)
    i+=1
 # find the count of the digit
num=int(input('Enter the number: '))
count=0
while num!=0:
    num//=10
    count+=1
print(count)
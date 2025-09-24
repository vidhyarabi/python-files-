def sum(lower,upper):
    even=0
    odd=0
    for i in range(lower,upper+1):
        if i%2==0:
            even+=i
        else:
            odd+=i
    print('even sum= ',even)
    print('odd sum= ',odd)
sum(1,5)
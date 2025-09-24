# calculate the road tax of a bike
price=int(input('enter the price:'))
if price>100000:
    tax=(price*15/100)
elif price>50000:
    tax=price*10/100
else:
    tax=price*5/100
print('Tax amount is',tax)

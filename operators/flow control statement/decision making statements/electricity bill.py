# electricity bill
unit=int(input('Enter the unit of electricity: '))
if unit<100:
    amount=0
elif 100<unit<200:
    amount=(unit-100)*5
else:
    amount=(100*5)+((unit-200)*10)
print('Bill amount is',amount)
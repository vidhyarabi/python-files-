price=int(input('Enter original price: '))
discount=int(input('Enter discount percentage: '))
final_dis=price*(discount/100)
print('Discount:₹'+str(final_dis))
final_price=price-final_dis
print('Final price after discount:₹'+str(final_price))

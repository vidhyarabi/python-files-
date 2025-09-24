# 1 to 50 elements add to a list and sum
# even numbers find and add in a separate list and find the sum
# odd numbers in a list and sum
list=[]
even_numbers=[]
odd_numbers=[]
sum_1=0
sum_2=0
sum_3=0
for i in range(1,51):
    list.append(i)
    sum_1+=i
    if i%2==0:
        even_numbers.append(i)
        sum_2+=i
    else:
        odd_numbers.append(i)
        sum_3+=i
print(list)
print(even_numbers)
print(odd_numbers)
print('sum of list',sum_1)
print('sum of even numbers',sum_2)
print('sum of odd numbers',sum_3)
#  or print(sum(list)) , print(sum(even_number)) , print(sum(odd_number))
#  here no need to form a separate sum variable to find the sum , simply at the end use the sum function
#  1 to 25 even numbers

lst=[i for i in range(1,26) if i%2==0]
print(lst)

# 1 to 20 odd numbers

lst1=[i for i in range(1,21) if i%2==1]
print(lst1)

# 1 to 50 divisible by 5

lst2=[i for i in range(1,51) if i%5==0]
print(lst2)

# 1 to 20 even number square

lst3=[i**2 for i in range(1,21) if i%2==0]
print(lst3)

# previous q even number too print
lst4=[(i,i**2) for i in range(1,21) if i%2==0]
print(lst4)
# a=5
# b=3
# c=2
# x=0
# if a>b:
#     if b<c:
#         x=x+3
#     elif c>b:
#         x=x+4
#     else:
#         x=x+5
# else:
#     x=x+2

def yr():
    year=int(input('Enter the year'))
    if year%4==0:
        print(year,'is a leap year')
    else:
        print(year,'not a leap year')
yr()
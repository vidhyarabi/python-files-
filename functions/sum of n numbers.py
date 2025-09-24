  # def sum():
#     num=int(input("Enter the number: "))
#     su=0
#     for i in range(1,num+1):
#         su+=i
#     print(su)
# sum()

# def sum(num):
#     su=0
#     for i in range(1,num+1):
#         su+=i
#     print(su)
# sum(4)

def sum(num):
    su=0
    for i in range(1,num+1):
        su+=i
    return su
data=sum(4)
print(data)
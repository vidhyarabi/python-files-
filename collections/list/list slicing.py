# list slicing

list=[1,5,40,53,20,70,44,20,55,44,33,23]
print(list[3:5])
print(list[0:5])
print(list[0:12])
print(list[5:]) # [ from start point to the end of the list]
print(list[:6]) # index 0 to stop point
print(list[:]) # list full print
print(list[1:7:2]) # here the third value is the step ==> 1,3,5
print(list[2::3])
print(list[:7:2])
print(list[::4]) # index 0 to end with step 4
print(list[-1]) # last element
print(list[-5])
print(list[-1:-5]) # slicing always works from left to right , so the output is an empty list
print(list[-5:-1]) # it will work cause it is from left to right
print(list[::-1])
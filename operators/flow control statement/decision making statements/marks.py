# find the total mark of 4 subjects and find the total ,  then total >=180 = A+ , total>=160-179 = A , total>=140-159 B+, etc
sub1=int(input('Enter sub1 mark:'))
sub2=int(input('enter sub2 mark: '))
sub3=int(input('enter sub3 mark: '))
sub4=int(input('Enter sub4 mark: '))
total=sub1+sub2+sub3+sub4
print('total mark=',total)
if total>=180:
    print('A+')
elif 160<=total<=179:  # elif total>=160
    print('A')
elif 140<=total<=159:#elif total>=140 these all are correct to cause in python its a line by line interpreter
    print('B+')
elif 120<=total<=139:
    print('B')
elif 100<=total<=119:
    print('C+')
elif 80<=total<=99:
    print("C")
else:
    print('FAIL')
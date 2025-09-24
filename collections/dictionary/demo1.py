# first recursive character - first repeated character
pattern='ABCDFCBSDFGHJIOP'
dic={}
for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        print('first recursive character is', i)
        break


#  list -[] read an element from the user and if it is in the list then print 'element found' else 'not found'

lst=[1,3,5,6,7,8,9,10,15,20,23,45,50]
num=int(input('Enter the number: '))
for i in lst:
    if num==i:
        print('element found')
        break
else:
    print('element not found')
#  without using for loop
if num in lst:
    print('found')
else:
    print('not found')

#
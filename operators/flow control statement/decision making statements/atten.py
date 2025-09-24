clss=int(input('NUmber of classes held: '))
attended=int(input('Number of classes attended: '))
percent=attended*100/clss
print('percentage is',percent)
if percent>75:
    print('allowed to sit in exam')
else:
    print('Not allowed to sit in exam')
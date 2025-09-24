# copy the file fruits but remove apple from it before copying

f=open('fruits','r')
f1=open('fruit_copy','w')
for i in f:
    if i!='apple\n':
        f1.write(i)
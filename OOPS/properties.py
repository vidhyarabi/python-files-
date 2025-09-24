class A:
    def printa(self,num1):
        self.num1=num1
        print('inside class A',self.num1)


class B(A):
    def printb(self,num2):
        self.num2=num2
        print('inside class B',self.num2)

obj1=B()
obj1.printb(20)
obj1.printa(30)
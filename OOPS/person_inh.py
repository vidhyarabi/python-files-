class person:
    def setvalue(self,fname,lname,age,location):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.location=location

class employee(person):
    def setvalue1(self,id,prof,dept,salary):
        self.id=id
        self.prof=prof
        self.dept=dept
        self.salary=salary
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.dept,self.salary,self.location)

object1=employee()
object1.setvalue('vinay','k','22','ern')
object1.setvalue1(101,'bigdata','engineer',3000)
object1.printvalue()
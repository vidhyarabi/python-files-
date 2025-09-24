

class person:
    def __init__(self,id,fname,lname,age,prof):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof

    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.prof)


per1=person(101,'vinay','v',22,'bigdata')
per1.printvalue()

per2=person(202,'vijay','h',33,'python')
per2.printvalue()
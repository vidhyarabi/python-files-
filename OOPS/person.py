class person:
    def setvalue(self,fname,lname,age,gender,location):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender
        self.loc=location
    def printvalue(self):
        print(self.fname,self.lname,self.age,self.gender,self.loc)
person1=person()
person1.setvalue('vinay','k','30','G','ernkl')
person1.printvalue()

person2=person()
person2.setvalue('anu','p','29','G','ernkl')
person2.printvalue()
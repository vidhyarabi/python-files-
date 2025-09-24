# employee class define with details - id,f name,l name,age,prof,dep(same),company name(same),salary)
class employee:
    company_name='Info'
    dep_name='data'
    def details(self,fname,lname,age,prof,salary):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.salary=salary

    def value(self):
        print(self.fname,self.lname,self.age,self.prof,employee.company_name,employee.dep_name,self.salary)

employee1=employee()
employee1.details('vid','rab','22','prog','20k')
employee1.value()

employee2=employee()
employee2.details('vidh','ra','23','eng','30k')
employee2.value()

employee3=employee()
employee3.details('vi','r','24','teac','34k')
employee3.value()

employee4=employee()
employee4.details('va','ri','30','prin','20k')
employee4.value()

employee5=employee()
employee5.details('vip','in','31','cont','50k')
employee5.value()
class student:
    def detail(self,id,fname,lname,age,course,coll_name):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course
        self.coll_name=coll_name
    def intern(self):
        print(self.id,self.fname,self.lname,self.age,self.course,self.coll_name)
student1=student()
student1.detail('1','vid','r','22','maths','a')
student1.intern()

student2=student()
student2.detail('2','vig','s','25','btech','b')
student2.intern()

student3=student()
student3.detail('3','meen','v','23','eng','c')
student3.intern()

student4=student()
student4.detail('4','viv','ab','2','history','d')
student4.intern()

student5=student()
student5.detail('4','vibi','c','24','bcom','e')
student5.intern()


class employee:
    name=""
    id=0
    def __init__(self,n,num):
        self.name=n
        self.id=num
    def display(self):
        print("Your name is : ",self.name)
        print("Your ID number is : ",self.id)

class person(employee):
    gender=""
    age=0
    def __init__(self,g,a,nm,numb):
        super().__init__(nm,numb)
        self.gender=g
        self.age=a
    def display(self):
        super().display()
        print("Your age is : ",self.age)
        print("Gender : ",self.gender)

fullname=input("Enter your full name:\n")
idnumber=int(input("Enter your id number:\n"))
age=int(input("Enter your age:\n"))
gender=input("Enter your gender:\n")
ob1=person(gender,age,fullname,idnumber)
ob1.display()


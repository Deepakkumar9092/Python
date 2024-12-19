

        

# class Stduent:
#     name=input("Enter your name")

# s1=Stduent()
# print(s1.name)

# s2=Stduent()
# print(s1.name)

#Constructor
# class Teacher:

#     # id=324

#     def __init__(self,fullname):
#         self.id=fullname
#         print("This is in danger jone")

#         t1=Teacher(2343)
#         print(t1)

from concurrent.futures.process import _MAX_WINDOWS_WORKERS


class Student:
    #default constructor
    def __init__(self):
        pass

    coll_name="Arya College" #Class Attribute
    #Parameterized Constructor
    def __init__(self, fullname, marks):
        self.name=fullname
        self.marks=marks
        print("This is in danger zone")
    
    def welcomr(self):
        print("Welcome Student",self.name)

    def get_marks(self):
        return self.marks
    
s1=Student("Deepak",65)
print(s1.name,s1.marks)
s2=Student("Himanshu",566)
print(s2.name,s2.marks)

s2.welcomr()
print(s2.get_marks())#If you returning something in function so you'll definitely print your function


#Create a class and store a name with 3 different subject marks
class Stude:
    def __init__(self, name, physics, maths, english):
        self.name = name
        self.physics = physics
        self.maths = maths
        self.english = english

s4 = Stude("Deepak",89,90,99)
print(s4.name,s4.english,s4.maths,s4.physics)

class Studen:
    @staticmethod
    def hello():
        print("This is static method")

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum+=i
        print("Hii",self.name,"Your Average marks is",sum/3)


s5 = Studen("Deepak",[89,90,92])
s5.hello()
print(s5.name,s5.marks)
s5.name="Tandulkar"
s5.get_avg()

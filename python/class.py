# class Person:
#     name = "anominious"
#     def changeName(self, name):
#         self.__class__.name="Deepak"# __class__

# p1 = Person()
# p1.changeName("Deepak")
# print(p1.name)
# print(Person.name)

class Student:
    def __init__(self, phy, che, maths):
        self.phy = phy
        self.che = che
        self.maths = maths
    @property #when you can in any providing parameter it will change automatically and start working for all new data providing
    def percentage(self):
        return str((self.phy + self.che + self.maths)/3)+"%"
    
stu = Student(89,90,98)
stu.phy = 70
print(stu.percentage)

# print(1 + 2) # for integer
# # print("Deepak" + 23)  throwing error
print([12,23,34]+[42,23,34])#for list
print((2,3,400,5)+(23,34,232))  #for tuple

#Inheritance - It is to inherit one class properties to another class 
# single and Multi_level Inheritance
# class Car:
#     type = "DIesel"
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("Car Started")
#     @staticmethod
#     def stop():
#         print("Car Stopped")

# class Toyota(Car):
#     def __init__(self, name):
#        self.name = name
#        super().start() #super() method used
#        super().stop()
    

# t1 = Toyota("Fortunar")
# print(t1.type)

# class Fortunar(Toyota):
#     def __init__(self, type):
#         self.type = type

# F1 = Fortunar("Petrol")
# F1.start()
# print(F1.type())

# T1 = Toyota("Fortunar") 
# T2 = Toyota("Mercedise")

# # print(T1.name)
# # print(T2.name)    
# print(T1.name)    
# T1.start()
# print(T2.name)
# T2.stop()

#Multiple Inheritance - Two or more parent class and one derived class
# class A:
#     Value = "this is A class Properties"
# class B:
#     value2 ="this is B class properites"

# class C(A,B):
#    value3= "This is Child class of A and B"

# C1 = C()
# print(C1.Value)
# print(C1.value2)
# print(C1.value3)



#del keyword
# class Student:
#     def __init__(self, name):
#         self.name = name
    
# s1 = Student("Deepak")
# print(s1.name)

# del s1.name
# print(s1.name)
        
#Private Attribute and Keywords
#Conceptual Implementation in Python
#Private attributes and methods are meant to be used only within the class and are not accessible from outside the class
# class Account:
#     # __name = "Arya College"
    
#     def __hello(self):
    
#         print("This is Hello method")
    
#     def dev(self):
#         self.__hello()
#         print("This is very dangerous situation")


# a1 = Account()
# print(a1.dev())
# print(a1.__hello)      
# print(a1.__name)

#Complex Number
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
    
#     def showImg(self):
#         print(self.real,"i +",self.img,"j")
    
#     def __add__(self, num2):# for adding complex real to real number and imaginary to imaginary number
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
#     def __sub__(self, num): # For subtract two real number and imaginary 
#         newReal = self.real - num.real
#         newImg = self.img - num.img
#         return Complex(newReal, newImg)
    
#     def __mul__(self, num): # For multiply real and img number
#         newReal = self.real * num.real
#         newImg = self.img * num.img
#         return Complex(newReal, newImg)
    
#     def __truediv__(self, num): # For division 
#         newReal = self.real / num.real
#         newImg = self.img / num.img
#         return Complex(newReal, newImg)
    
#     def __mod__(self, num): # For modula 
#         newReal = self.real % num.real
#         newImg = self.img % num.img
#         return Complex(newReal, newImg)
    
# num = Complex(4, 5)
# num.showImg()
# num1 = Complex(34, 32)
# num1.showImg()
        
# #Dunder Function
# num2 = num + num1
# num2.showImg()

# num3 = num - num1
# num3.showImg()

# num4 = num * num1
# num4.showImg()

# num5 = num / num1
# num5.showImg()

# num6 = num % num1
# num6.showImg()

# Q circle of the paramenter and radius
# class Radius:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         # return (22/7) * self.radius ** 2 
#         return 3.174 * self.radius ** 2    
#     def parameter(self):
#         return 2 * 3.174 * self.radius

# r1 = Radius(5)
# print(r1.area())
# print(r1.parameter())


#Q2 . Define a Employee class with attributes role, department & salary. This class will showDetail() method 
class Employee:
    def __init__(self, role ,dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal

    def showDetail(self):
        print("role = ", self.role)
        print("dept = ", self.dept)
        print("sal =", self.sal)
    
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","Developer","24000")
 
e2 = Engineer("Deepak","24")
print("name =",e2.name)
print("age = ",e2.age)
e2.showDetail()

        
# Using Dunder __gt__ to find Order class price 
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, ord1):
       return self.price > ord1.price
       
        
order1 = Order("Banana", 34)
order2 = Order("Cocunut", 35)
print(order1 > order2)


# Conditional Statement
# if-elif-else(Syntax)
#if(statement1)
#elseif(statement2)
#else(statement3)

# program for eligible for licence or not
# age=19
# age=int(input("Enter your age: "))
# if(age>=18):
#     print("You are eligible for Vote & Apply for Licence")
# elif(age<18):
#     print("You are not eligible for Vote & for Licence")
# else:
#     print("Please type valid number")

# #program for signal light
# light=input("Enter color ")
# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# elif(light=="yellow"):
#     print("wait/look")
# else:
#     print("light is broken")#indentation means proper spacing 

#  Note: The main difference b/w if and elif is if check statement always but elif checks when if condition takes false 

# Grade System of Student write program for
# print("Enter your Percentage")
# marks=int(input("Check Your Grade : "))
# if(marks>=90):
#     grade="A"
# elif(marks>90 or marks>=80):
#     grade= "B"
# elif(marks>80 or marks>=70):
#     grade="C"
# elif(marks>60 or marks>=50):
#     grade="D"
# else:
#     print("Fail")

# print("Grade of the student ", grade)

# Program for Even and Odd number
number=int(input("Enter number"))
if(number%2==0):
    print("Even")
elif(number%3==0):
    print("Odd")
else:
    print("Prime Number")    

#WAP to find gratest of 3 numbers entered by user
a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))

if(a>b and a>c):
    print("a is greater than b and c :",a)
elif(b>a and b>c):
    print("b is greater than a and c :", b)
else:
    print("C is greater than both a and b :",c)

#WPA to check if a number is a multiple by 7 or not
number=int(input("enter number : "))
if(number % 7==0):
    print("It is divisible by 7")
else: 
    print("It is not divisible by 7")
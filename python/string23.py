# #reverse string
# name=input("enter your name :")
# print(name[::-1])

# #slicing string
# name="deepak"#-6,-5,-4,-3,-2,-1
# print(name[0:3])
# print(name[2:5])
# print(name[1:4])
# print(name[0:6])
# print(name[-3:-1])

# String function
name="my name is Deepak Kumar I am from Jharkhand"
print(name.endswith("pa"))#endswith()
print(name.startswith("dee"))
print(name.capitalize())
print(name.replace("my","I"))
print(name.find("z"))
print(name.count("Deepak"))


#WAP to input user's first name & print string length
first_name=input("enter first name ")
print(len(first_name))


#WAP to find the occurence of '$' in a String
str="dee$ dsl$ ksdj$ln$ klds$"
print("Count of $ sign is :" ,str.count("$"))
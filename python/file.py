# open,read & close file

"""
we have to open a file before reading and writting
f=open("file_name","mode")
--------sample.txt, r:read mode // by default read python is shown mod
        read.doc,   w: write mode

        data = f.read()
        f.close()
"""
# f = open("read.txt","rt")
# data=f.read(5)
# de=f.readline()
# print(de)
# print(data)
# print(type(data))
# f.close()

# write mode
# f=open("read.txt","a")#a is showing for append next sentence
# f.write("\nI am from Jharkhand")
# f.close()

# d=open("sample.txt","r+") # r+ append from starting sentence
# # d.write("Jharkhand Washi")
# t=d.read()
# print(t)
# d.close()

#w+ mode trucate everything first then you write and read 
# c=open("dample.txt","w+")
# w=c.read()
# print(w)
# c.write("Deepak")
# c.close()

#with syntax
# with open("dample.txt","r") as l:
#     g= l.read()
#     print(g)
#     l.close()

#Deleting the file
# import os
# os.remove("dample.txt")

#practice question
with open("practice.txt","r") as p:
#     p.write("Hii EveryOne\nWe are learning File i/o \n")
#     p.write("Using Python \n I like programming in Python")
# we want to replace Python to Java
        data = p.read()

        new_data=data.replace("Python","Java")
        print(new_data)


x=[2,4,5,6]
y=x
x[0]=90
print(y)



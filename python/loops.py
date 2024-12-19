# Loops in Python

# Loops are used to repeat instructions.

# print hello 5 times
# print numbers from 1 to 5

# while condition :

# Let‘s Practice

# Print numbers from 1 to 100.

# Print the elements of the following list using a loop:

# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# Print numbers from 100 to 1.

# Print the multiplication table of a number n.

# Search for a number x in this tuple using loop:

# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# count=1
# while count<=5:
#     print("Deepak")
#     count+=1
# print(count)

# i=1
# while i<=10:
#     print("Table",i*2)
#     i+=1

    
#####Practice Question By using While Loop#############
# Print numbers from 1 to 100.
# num=1
# while num<=100:
#     print(num)
#     num +=1
# print("Loop Ended")

# Print numbers from 100 to 1.
# i=100
# while i>=1:
#     print(i)
#     i -= 1

# Print the multiplication table of a number n.
# n = int(input("Enter the number for the table you want: "))
# i = 1
# while i <= 10:
#     print({n*i})
#     i += 1


####Print the length of list using while loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# nums=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# herose=["IronMan","Sachin Tendulkar", "Shiva Rao","VhaleRao"]

# inx=0
# while inx < len(herose):
#     print(herose[inx])
#     inx+=1

#Search for a number X in this tuple using while loop
# (1,4,9, 16,25,36,49,64,81,100)
# for printing tuple
# tup=(1,4,9, 16,25,36,49,64,81,100)
# x=int(input("Enter number"))
# i=0
# while i<len(tup):
#     if(tup[i]==x):
#         print("Found at index",i)
#         break
#     i+=1

#continue
# i=1
# while i<=50:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

    ########For Loop #########
# list=[3,43,12,34,45,45]
# for el in list:
#     print(el)

# vege=("potato","tomato","ladisfinger","cocounut")
# for v in vege:
#     print(v)

#Search for a number X in this tuple using while loop
# (1,4,9, 16,25,36,49,64,81,100)
# tup=(1,4,9,16,25,36,49,64,81,100,16)
# i=0
# x=16
# for el in tup:
#     if(el==x):
#         print("Found at index",i)
#         break
#     i+=1

#Search for a number in this list using while loop
# (1,4,9, 16,25,36,49,64,81,100)
# tup=(1,4,9, 16,25,36,49,64,81,100)
# i=0
# for el in tup:
#     print(tup[i])
#     i+=1

#range(start?,stop, step;])
# seq=range(10)
# for i in seq:
#     print(i)

# for i in range(5):
#     print(i) 

    #total sum of all n elements
# n=5
# sum=0
# i=1
# while i<=n:
#     sum += i
#     i+=1
# print(sum)
   

# for i in range(n+1):
#     sum+=i
# print("total sum of all elements",sum)

#factorial of n number
# num=4
# fact=1
# i=1
# while i<=num:
#     fact *= i
#     i += 1
# print("Factorial is ",fact)

#By using for loop
n=5
fact=1
for el in range(1, n+1):
    fact *= el
print("factorial is :", fact)
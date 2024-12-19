# A built-in data type that lets us create immutable sequences of values
# tup=(32,34,21,34,54,) #tup[0] tup[1]

tup=(23,43,12,34,80)
print(type(tup),tup)
print(tup[0])

# it follows
# ()
# (23,)
sum_of_elements = sum(tup)
print("Sum of elements in the tuple: ", sum_of_elements)

dup=(23,43,2,4,12,43,34,23)
print(dup[1:4])
print(dup.index(4)) 
print(dup.count(23))
#Tuples methods
# index(ele)
# count(ele)

# print list of movies 
# movies=()
# mov1=input("enter your 1st movie")
# mov2=input("enter your second movie")
# mov3=input("enter your third movie")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)
# print(type(movies))

#wap to check if a list contains a palindrome of elements. (Hint: use copy() method)
list1= ["m","a","a","m"]
list2=[2,4,1]

copy_list=list1.copy()
list1.reverse()
if(copy_list==list1):
    print("List 1 : It is palindrome")
else:
    print("It is not palindrome")

copy_list2=list2.copy()
list2.reverse()
if(copy_list2==list2):
    print("This is palindrome")
else:
    print("It is not palindrome")

# WAP to count the number of student with "A" grade of the following tuple
tup=("A","B","c","A","A","D","A","F","A")
print(tup.count("A"));

#Store the above values in a list & sort them "A" to "D".
lis=["A","B","C","A","A","D","A","F","A"]
print(lis)
lis.sort()
print(lis)


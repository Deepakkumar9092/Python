# A list is a built-in data type that stores set of values
# it can store elements of different types(integer, float, string,etc)
# eg - marks=[23,43,54,54,34] marks[0],marks[1]
# student=["karan",89,"Delhi"]
# student[0]="Arjun"

marks=[56.45,43.4,67.89,90.94,43.6]
print(marks)
print(type(marks))
#List is Mutable you can change very easily but string is immutable once you define a string so no one change 
karan=[90.43,"Karan",101]
print(karan)
print(len(karan))
karan[1]="Karana"
print(karan)

# List Slicing
number=[23,32,34,45,23.32]
danger=number[0:3]
print(danger)

#append()
list=[23,34,231,34]
list.append(2434)
print(list)

#sort() is in ascending order
list.sort()
print(list)

#sort in descending order
list.sort(reverse=True)
print("Descending order: ",list)

#reverse list
list.reverse()
print("reverse list", list)

#insert(index,element)
list.insert(2,340)
print("inserting value of index 2 is: ",list)

#remove() remove first occurence of element[3,2,5,3]
value=[23,43,12,34]
value.remove(43)
print(value)

value.pop(0)
print("pop value of index 0 ",value)

print("Count of 23 in the list is: ", value.count(23))# count method is to count the number of available element in your list

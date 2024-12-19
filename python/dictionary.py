# Dictionaries are used to store data values in key:value pairs

# “key” : value

# They are unordered, mutable(changeable) & don’t allow duplicate keys

# dict[”name”], dict[”cgpa”], dict[”marks”]

# dict[”key”] =

# “value” #to assign or add new

info={
    "name": "Deepak",
    "coding language":["C++", "Java", "Python", "SpringBoot"],
    "language":"(English,Hindi)",
    "vill": "Purnatham",
    "Po+ps": "Chandwara",
    "Dist": "Koderma",
    "state": "Jharkhand",
    "country": "India"
}
print(info)
print(info["name"])
print(info["Dist"])
info["name"]="Kumar"
print(info)
# Nested Dictionaries
student={
    "name":"Deepak",
    "score":{
        "math":100,
        "che":324,
        "phy":43
    },
    "vill":"India"
}
print(student)
print(type(student))

# Dictionary Methods

# myDict.keys( ) #returns all keys

# myDict.items( ) #returns all (key, val) pairs as tuples

# myDict.update( newDict ) #inserts the specified items to the dictionary
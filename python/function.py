#function definition
# def sumd(a, b):
#     return a+b
    

# d = sumd(23, 43)#function call,argument 
# print(d)
# e=sumd(45, 34)
# print(e)

# def hello():
#     print("hello")
# hello()
# hello()

#average of 3 numbers
# def cal_avg(a, b, c):
#     sum=a + b + c
#     avg=sum / 3
#     return avg
#     # print(avg)
# print(cal_avg(2,3,5))

#print length of cities is given by
cities=["Mumbai","Chennai","Bangalore","Noida","Pune","Gurgaon"]
heros=["shaktiman","Batman","Junior ji"]
print(heros[0],end=" ")
print(cities[0],end=" ")

def leng(list):
    print(len(list))
    return len(list)
leng(cities)
leng(heros)

def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(cities)
# print_list(heros)
leng(heros)

#for factorial 
def factor(n):
    fact=1
    for el in range(1,n+1):
        fact *= el
    print(fact)

factor(5)
factor(23)

#convert usd to inr
def convertor(usd_val):
    inr_val=usd_val*84.44
    print(usd_val,"USD =",inr_val,"INR" )
convertor(130)

#odd and even string
def odd(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")
def even(n):
    if(n%3==0):
        print("Odd Number")
    else:
        print("Prime nuber")
odd(41)
even(35)

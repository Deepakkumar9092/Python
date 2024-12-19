
# def show(n):
#     if(n==0):#Base case
#         return
#     print(n)
#     show(n-1)
# show(4)

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(4))


#print first n natural number
def cal_sum(n):
    if(n==0):
        return 0
    # print(n)
    return cal_sum(n-1) + n
sum=cal_sum(10)
print(sum)
# cal_sum(5)

#Recursive function for print all elements
def print_ele(list, ind=0):
    if(ind==len(list)):
        return 0
    print(list[ind])
    print_ele(list,ind+1)

fruits=["mangao","banana","Papaya"]
print_ele(fruits)
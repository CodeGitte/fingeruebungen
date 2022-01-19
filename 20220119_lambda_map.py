#playing around with map & lambda 

#creating some random list
from numpy import random
numbers = random.randint(100, size=(5))
print(numbers)

#creating a function with a for loop
def plus_ten(list):
    list_new = []
    for i in list:
        x = i + 10
        list_new.append(x)
    return list_new
print(plus_ten(numbers))

#using map and lambda
#The map() function in Python takes in a function and a list as an argument. 
#The function is called with a lambda function and a list and a new list is returned which contains all the lambda modified items returned by that function for each item
numbers_ten = list(map(lambda x: x+10, numbers))
print(numbers_ten)
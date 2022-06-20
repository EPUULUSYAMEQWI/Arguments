def product_and_greeting(*args,**kwargs):
    product=1
    for num in args:
        product*=num
    print(f"Hello {kwargs['name']} and you are {kwargs['age']}years old. The result is {product}")
    print(f"Hello{kwargs['name']} and you come from {kwargs['country']}. The result is {product}")

# create a function that takes in two numbers and adds and check weather ><=to 10 and prints it out.
def numbers(a,b):
    sum=a+b
    if sum>10:
        print("sum is greater")


    elif sum<10:
        print("sum is less than")


    
    else:
        print("sum is equal")
numbers(3,8)

# # takes in a range of dictionary from 1 to 15 and prints it's square
def number():
    K={i:i**2 for i in  range(1,16)}
    print(K)
number()
         
 # create a function from two list without losing duplicate values.
def two_list():
    one=[10,20,30,40,30]
    two=["Me","You","Us"]
    my_dict={}
    for i in one:
        for z in two:
            if i not in my_dict.values():
                my_dict[i]=z
            print(my_dict)
two_list()
    #    1. #Write a function that takes one argument as a list a=[2,4,6,8] and remove the second 
#last item from that list and returns the whole list without the removed item

def remove_items(list):
    list.remove(list[-2])
    return list
list1=[2,4,5,6,7]
print(remove_items (list=list1))

   
   
 
# 2.# Write a python program that has a list days = ["Monday","Tuesday","Friday","Monday"] and
#counts the number occurrences of Monday

def list_days():
    three=["Monday","Tuesday","Friday","Monday","Thursday","Monday"]
    w=three.count("Monday")
    print(w)
list_days()

# 3.#Write a python function named smallest that accepts a list of unsorted integers and returns
# #the smallest number in the list.Example:smallest([3,6,8,2,4,1,5,7]) returns 3

def smallest(list):
    print(min(list))
list=[7,5,8,0,2,1]
smallest(list)

# 4.Write a function named divisible_by_seven that;using the range function and a for loop
# #returns a list containing all the numbers between 100 and 200 that are divisible by 7

def divisible_by_seven():
    for w in range(100,200):
        if w %7==0:
            print(w)
divisible_by_seven()

# 5.#Write a python program that takes two inputs(as int) from a user and adds
# #the 2 numbers,checks if the sum is greater than 10,less than 10 or equal 10

def interger_numbers(c,d):
    sum=c+d
    if sum <10:
        print("sum is greater")
    elif sum >10:
        print("sum is less")
    else:
        print("sum is equal")
interger_numbers(1,2)

# 6.Write a function that takes one argument which is a list a=[1,2,3,4,5] and
#returns True if 4 is present in the list and False if 4 is not in the list

def numbers():
    list=[1,2,3,4,5]
    if 4 in list:
            print("true")
    else:
        print("false")
numbers()

#7. #Write a function that takes one argument which is a list
#fruits=["apples","grapes","pineapple"]and removes the last fruit from the list.
 
def fruits():
    fruits=['mango','banana','kiwi','apple']
    fruits.remove('apple')
    print(fruits)
fruits()

#8#Write a python program that takes in a list of cars,cars=["Ford","BMW","vOLVO"]
#and returns a sorted list then returns tand prints a statement after each check.

def vehicle():
    cars=['bmw','sunny','toyota','ford','harrier','jeep']
    cars.sort()
    print(cars)

vehicle()

   

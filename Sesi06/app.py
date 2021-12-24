def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'

# for char in my_generator():
#     print(char)

# print(list(my_generator()))

# print(next(my_generator()))


# def counter_generator(low, high):
#     while low <= high:
#        yield low
#        low += 1

# for i in counter_generator(5,10):
#   print(i, end=' ')

# counter_generator(1, 10)


def square(nums):
    for num in nums:
        yield(num*num)

nums = [1,2,3,4,5].__iter__()

print(square(nums))
print(square(nums).__next__())
print(next(square(nums)))
print(next(square(nums)))
print(next(square(nums)))
print(next(square(nums)))

# List comperhension
squared_nums = [y * y for y in [1,2,3,4,5]]
# print(squared_nums)

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

# a = greet_bob(say_hello)
# print(a)

# b = greet_bob(be_awesome)
# print(b)

# Inner Functions

# def parent():
#     print("Printing from the parent () function")

#     def first_child():
#         print("Printing from the first_child() function")
#     def second_child():
#         print("Printing from the second_child() function")
    
#     second_child()
#     first_child()

# parent()

def parent(num):
    def first_child():
        return "Hi, Iam Emma"
    
    def second_child():
        return "Call me Liam"
    
    if num == 1:
        return first_child
    else:
        return second_child

# parent_result = parent(1)
# print(parent_result())

first = parent(1)
first()
# print(first())

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = my_decorator(say_whee)

# say_whee()

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()
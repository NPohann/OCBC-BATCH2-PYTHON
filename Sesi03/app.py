import person


# Function in Python
def my_function(p, l):
    "Function to calculate area of a square"
    print(p * l)
    return p * l

def printme( str_input ):
    "This prints a passed string into this function"
    print(str_input)

# my_function(9, 2)
# print(my_function.__doc__)    

printme(100)
print(printme.__doc__)

printme("I'm first call to user defined function!")
printme("Again second call to the same function")

# Pass Reference & Value
def changeme (mylist):
    "This changes a passed list into this function"
    mylist = mylist+[1,2,3,4]
    print("\nValues inside the function : ", mylist)
    return mylist

mylist = [10,20,30]
print("\nValues outside the function - before : ", mylist)
mylist = changeme(mylist)
print("\nValues outside the function - after : ", mylist)

luas = my_function(10, 3)
print(f"Luas persegi panjang adalah {luas}")

def save_data(name, age):
    print(f"Nama : {name}")
    print(f"Age + 10 = {age + 10}")

save_data(age=20, name="Adi")

# Default Argument
# def printinfo(name, age=26):
#     "This prints a passed info into this function"
#     print("Name: ", name)   
#     print("Age: ", age)   
#     return


# Now you can call printinfo function
# printinfo( age=50, name="hacktiv8" )
# printinfo( name="hacktiv" )

# Multiple Arguments
def printinfo( arg1, *vartuple ):
    # def printinfo(arg1, arg2, arg3, arg4):
   '''This prints a variable passed arguments'''
   print('arg1     : ', arg1)
   print('vartuple : ', vartuple)
   print('')
   
   for var in vartuple:
      print('isi vartuple : ', var) 

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )


# Return Statement
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    return total

# Now you can call sum function
total = sum(10, 20)
print("Result function : ", total)

# Global Variables
total = 0
def sum(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function local total : ", total)

sum( 10, 20 )
print("Outside the function global total : ", total)

print(person.devices)

import person2
print(person2.brands)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


# GETING TYPE
x = 5
y = "John"
print(type(x))
print(type(y))

# CASE-SENSETIVE
a = 4
A = "Sally"
print(a)
print(A)


# MANY VALUES TO MULTIPLE VARIABLES
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# ONE VALUE TO MULTIPLE VARIABLES
x = y = z = "Orange"
print(x)
print(y)
print(z)


# UNPACK A COLLECTION 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# GLOBAL KEYWORD
# x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
thistuple = ("apple", "banana", "cherry", "apple") #To create a tuple with only one item, have to add a comma
print(thistuple)
print(len(thistuple))

tuple1 = ("abc", 34, True, 40, "male")

# TUPLE CONSTRUCTOR
thistuple = tuple(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
print(thistuple)


# ACCESS ITEMS
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:4])
print(thistuple[:3])
print(thistuple[5:])


# CHECKING
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")


# CHANGE TUPLE
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


# ADD ITEM
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)


# REMOVE ITEM
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)


# DELETE TUPLE
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


# UNPACKING TUPLE
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


# LOOP
for x in fruits:
    print(x, end = " ")

for i in range(len(thistuple)):
    print(thistuple[i])


# JOIN TUPLES
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)


# MULTIPLY TUPLE
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
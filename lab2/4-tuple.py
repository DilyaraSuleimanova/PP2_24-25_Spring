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


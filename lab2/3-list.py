thislist = ["apple", "banana", True, 16, 3.14]
print(thislist)
print(len(thislist))
print(type(thislist))


# LIST CONSTRUCTOR
thislist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
print(thislist)


# ACCESS ITEMS
print(thislist[-1])
print(thislist[:4])
print(thislist[2:])
print(thislist[2:5])
print(thislist[-4:-1])


# CHECKING
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


# CHANGE ITEMS
thislist = ["apple", "banana", "cherry", "orange"]
thislist[1] = "blackcurrant"
print(thislist)
thislist[1:3] = ["redcurrant", "watermelon"]
print(thislist)
thislist[1:2] = ["kiwi", "melon", "mango"]
print(thislist)


# ADD ITEMS
thislist = ["apple", "banana", "cherry", "watermelon"]
thislist.insert(2, "watermelon")
thislist.append("orange")
print(thislist)
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # extend() can add any iterable object (tuples, sets, dictionaries etc.)
print(thislist)


# REMOVE ITEMS
thislist.remove("watermelon")
thislist.pop(1) # If do not specify the index, the pop() method removes the last item
del thislist[0] # The del keyword can also delete the list completely
print(thislist) 
thislist.clear() # Empty the list
print(thislist)


# LOOP IN LIST
thislist = ["apple", "banana", "cherry"]
# for x in thislist:       |  for i in range(len(thislist)):
#    print(x, end = ", ")  |      print(thislist[i], end = ", ")
[print(x, end = ", ") for x in thislist]


# LIST COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if "a" in x]
print(newlist)
''' SAME AS:
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
'''
newlist = [x for x in range(10)]
newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]


# SORT
thislist = ["orange", "mango", "kiwi"]
thislist.reverse() # regardless of the alphabet
print(thislist)
thislist.sort() # case sensitive; "thislist.sort(key = str.lower)" if start with lower case
print(thislist)
thislist.sort(reverse = True) # desc. order
print(thislist)


# COPY LIST
mylist = thislist.copy() # mylist = thislist[:] OR mylist = list(thislist)
print(mylist)


# JOIN LIST
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2 
# list1.extend(list2)
# for x in list2:
#   list1.append(x)
print(list3)



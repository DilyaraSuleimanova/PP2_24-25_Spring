thisset = {"apple", "banana", "cherry", "apple", 0} # no ducplicates
print(thisset)
thisset = {"apple", 3.14, "banana", "cherry", True, 1, 2, False, 0} # 1 and True same, 0 and False same
print(thisset)
print(len(thisset))


# LOOP
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


# CHECKING
print("banana" in thisset)
print("mango" not in thisset)


# ADD ITEM/SET/LIST...
thisset.add("orange")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


# REMOVE ITEM
thisset.remove("banana")
print(thisset)

thisset.discard("kiwi")
print(thisset)

x = thisset.pop() 
print(x)
print(thisset)

thisset.clear()
print(thisset)


# DELETE TUPLE
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the tuple no longer exists


# JOIN TUPLES
# The functions allow to join set with other data types
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2 # instead sign can use union(). 
print(set3)

set1.update(set2) # union() and update() will exclude any duplicate items.
print(set1)

set1 = {"apple", 1, "banana", "cherry", 0}
set2 = {False, "google", "microsoft", "apple", True}
set3 = set1.intersection(set2) # return a new set. Also can use '&' sign
print(set3)

set1.intersection_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) # can use '-' sign
print(set3)

set1.difference_update(set2)
print(set1)

set3 = set1.symmetric_difference(set2) # can use '^' sign
print(set3)

set1.symmetric_difference_update(set2)
print(set1)

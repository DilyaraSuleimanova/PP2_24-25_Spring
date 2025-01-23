thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))


# ACCESS ITEM
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

x = thisdict.keys()
print(x)

x = thisdict.values()
print(x) # before the change
thisdict["year"] = 2020
print(x) # after the change

x = thisdict.items()
print(x)


# CHECKING
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


# CHANGE VALUE
thisdict.update({"year": 2024})
print(thisdict)

thisdict["year"] = 2018
print(thisdict)


# ADD ITEM
thisdict["color"] = "red"
print(thisdict)

thisdict.update({"color": "green"})
print(thisdict)


# REMOVE ITEM
thisdict.pop("color")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["model"] # del thisdict deletes dict
print(thisdict)

thisdict.clear() # empty dict
print(thisdict)


# LOOP
for x in thisdict:
    print(x, end = " ")

for x in thisdict:
    print(thisdict[x], end = " ")

for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x, y)


# COPY DICT
mydict = thisdict.copy() # OR mydict = dict(thisdict)
print(mydict)



###############
# NESTED DICT #
###############

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# ACCESS ITEM
print(myfamily["child2"]["name"])

# LOOP
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
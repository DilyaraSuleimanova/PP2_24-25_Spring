fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


for x in "banana":
    print(x)


# BREAK STATEMENT
for x in fruits:
    print(x)
    if x == "banana":
        break

for x in fruits:
    print(x)
    if x == "banana":
        break


# CONTINUE STATEMENT
for x in fruits:
    if x == "banana":
        continue
    print(x)


# RANGE() FUNC.
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)


# ELSE IN FOR
for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")


# NESTED LOOP
adj = ["red", "big", "tasty"]

for x in adj:
    for y in fruits:
        print(x, y)


# PASS STATEMENT
for x in [0, 1, 2]:
    pass # to avoid getting an error
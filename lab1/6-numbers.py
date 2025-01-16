x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
x = float(x)

#convert from float to int:
y = int(y)

#convert from int to complex:
z = complex(x)

print(x)
print(y)
print(z)
print()

print(type(x))
print(type(y))
print(type(z))
print()



#   RANDOM  NUMBER
import random
print("Random number:")
print(random.randrange(1, 10))
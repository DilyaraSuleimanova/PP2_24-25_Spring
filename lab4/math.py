import math

# 1 task
deg = int(input("Degree: "))
rad = deg * math.pi / 180
print(f"Radian: {rad:.5}")


# 2 task 
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

s = (a + b) / 2 * h

print ("Area:", s)


# 3 task
sides = int(input("Number of sides: "))
length = int(input("The length of a side: "))

ctg = 1 / math.tan(180 / sides)
s = sides / 4 * (length ** 2) * ctg

print ("Area:", s)


# 4 task
base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))

s = base * height

print ("Area:", s)
# 1 task
def square(n):
    for i in range(n + 1):
        yield i * i

n = int(input("Enter n: "))
for x in square(n):
    print(x, end=" ")


# 2 task
def even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter n: "))
for x in even(n):
    print(x, end=" ")


# 3 task 
def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter n: "))
for x in divisible(n):
    print(x, end=" ")


# 4 task
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
    
a = int(input("Enter a: "))
b = int(input("Enter b: "))
for x in even(a, b):
    print(x, end=" ")


# 5 task
def rev(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter n: "))
for x in rev(n):
    print(x, end=" ")

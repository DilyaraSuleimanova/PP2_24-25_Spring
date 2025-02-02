# # 1 task
# class Str_convert:
#     def getstring(self):
#         self.string = input("Enter string: ")
    
#     def printstring(self):
#         print(f"Upper case string: {self.string.upper()}")

# str = Str_convert()
# str.getstring()
# str.printstring()


# # 2 task
# class Shape:
#     def __init__(self):
#         self.s_area = 0

#     def area(self):
#         return self.s_area


# class Square(Shape):
#     def __init__(self):
#         self.length = int(input("Square length: "))
#         super().__init__()

#     def area(self):
#         self.s_area = self.length ** 2
#         return super().area()
        

# square = Square()
# print("Area of square:", square.area())

        
# # 3 task

# class Rectangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.length = int(input("Rectangle length: "))
#         self.width = int(input("Rectangle width: "))

#     def area(self):
#         self.s_area = self.length * self.width
#         return super().area()
    

# rectangle = Rectangle()
# print("Area of rectangle:", rectangle.area())


# # 4 task
# from math import sqrt

# class Point:
#     x0 = 0
#     y0 = 0
#     def __init__(self):
#         self.x = int(input("x coordinate: "))
#         self.y = int(input("y coordinate: "))

#     def show(self):
#         print(f"Point coordinates ({self.x}, {self.y})")

#     def move(self):
#         global x0, y0
#         x0 = self.x
#         y0 = self.y
#         self.x = int(input("x coordinate: "))
#         self.y = int(input("y coordinate: "))

#     def dist(self):
#         self.distance = sqrt((x0 - self.x) ** 2 + (y0 - self.y) ** 2)
#         print("The distance between 2 points:", round(self.distance, 2))


# point = Point()
# point.show()
# point.move()
# point.dist()


# # 5 task
# class Account:
#     def __init__(self):
#         self.owner = input("Enter your name: ")
#         self.balance = float(input("Enter your balance: "))

#     def deposit(self):
#         amount = float(input("Deposit: "))
#         self.balance += amount
#         print("Your balance: ", self.balance, "\n")

#     def withdraw(self):
#         amount = float(input("Withdraw: "))
#         if amount > self.balance:
#             print("You can not exceed the available balance.")
#         else:
#             self.balance -= amount
#         print("Your balance: ", self.balance, "\n")

#     def choices(self):
#         exit_key = ""
#         while exit_key != "3":
#             choice = input("Choose option (1 - 3):\n\t1. Deposit \n\t2. Withdraw \n\t3. Finish operation\n")

#             if choice == "1":
#                 self.deposit()
#             elif choice == "2":
#                 self.withdraw()
#             elif choice == "3":
#                 break
#             else:
#                 print("Please choose again.")

# acc = Account()
# acc.choices()


# # 6 task
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def filt_prime(nums):
#     return list(filter(lambda x: is_prime(x), nums))

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# prime_numbers = filt_prime(numbers)
# print("Prime numbers:", prime_numbers)


            


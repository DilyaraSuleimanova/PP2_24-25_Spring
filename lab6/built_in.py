# 1 task
import math
entered_list = list(map(int, input("Enter list elements: ").split()))
new_list =  math.prod(entered_list)
print(new_list)


# 2 task
entered_string = input("Enter string: ")
upper_sum = 0
lower_sum = 0
for item in entered_string:
    if item.isupper():
        upper_sum += 1
    elif item.islower():
        lower_sum += 1
print(f"Upper case letters = {upper_sum}\nLower case letters = {lower_sum}")


# 3 task
entered_string = input("Enter string: ").lower()
reversed_string = ''.join(reversed(entered_string))
if entered_string == reversed_string:
    print("String is palindrome")
else:
    print("String is not palindrome")


# 4 task
import time
import math
entered_number = int(input("Enter number: "))
entered_millisec = int(input("Enter milliseconds: "))
time.sleep(entered_millisec / 1000)
print(f"Square root of {entered_number} after {entered_millisec} miliseconds is {math.sqrt(entered_number)}")


# 5 task
entered_tuple = tuple(input("Enter tuple elements: ").split())
print(all(entered_tuple))
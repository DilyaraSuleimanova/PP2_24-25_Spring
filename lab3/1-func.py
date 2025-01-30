# # 1 task
# def convert(grams):
#     ounces = 28.3495231 * grams
#     print (ounces)

# grams = int(input())
# convert(grams)


# # 2 task
# def to_C(F):
#     C = (5 / 9) * (F - 32)
#     return C

# F = int(input())
# print(to_C(F))


# # 3 task
# def solve(numheads, numlegs):
#     chickens = 2 * numheads - numlegs / 2
#     rabbits = numlegs / 2 - numheads
#     print ("rabbits =", rabbits, "\nchickens =", chickens)

# numheads = int(input("numheads = "))
# numlegs = int(input("numlegs = "))
# solve(numheads, numlegs)
# # x + y = numh        -->  x = numh - y         -->  x = 2numh - numl / 2
# # 1x + 2y = numl / 2  -->  numh + y = numl / 2  -->  y = numl / 2 - numh


# # 4 task
# def is_prime(nums):
#     prime_list = []
#     for i in nums:
#         if i % 2 == 0:
#             prime_list.append(i)
#     return prime_list

# entered_list = list(map(int, input("Enter numbers separated by space: ").split()))
# print(is_prime(entered_list))


# # 5 task


# # 6 task
# def rev_str(string):
#     string.reverse()
#     for word in string:
#         print(word, end=" ")

# list_str = input().split()
# rev_str(list_str)


# # 7 task
# def has_33(nums):
#     for i in range(1, len(nums)):
#         if nums[i - 1] == 3 == nums[i]:
#             return True
#     return False

# entered_list = list(map(int, input("Enter numbers separated by space: ").split()))
# print(has_33(entered_list))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))


# # 8 task
# def spy_game(nums):
#     spy = [x for x in nums if x == 0 or x == 7]
#     for i in range(2, len(spy)):
#         if spy[i - 2] == 0 == spy[i - 1] and spy[i] == 7:
#             return True
#     return False

# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))


# # 9 task
# def volume_sphere(r):
#     pi = 3.14
#     print (round(4 / 3 * pi * r ** 3, 2))

# radius = int(input("Radius: "))
# volume_sphere(radius)


# # 10 task
# def unique_elements(first_list):
#     new_list = [first_list[0]]
#     for item in first_list:
#         if item not in new_list:
#             new_list.append(item)
#     print("New list without duplicates:", new_list)

# enter_list = list(map(int, input("Enter numbers separated by space: ").split()))
# unique_elements(enter_list)


# # 11 task
# def polindrome(word):
#     new_word = word[::-1]
#     print("Polindrome" if new_word == word else "Not polindrome")

# word = input("Enter word: ")
# polindrome(word)


# # 12 task
# def histogram(values):
#     for i in values:
#         for j in range(i):
#             print("*", end="")
#         print()

# nums = list(map(int, input("Enter numbers separated by space: ").split()))
# histogram(nums)


# # 13 task
# import random as rand
# def guess_num():
#     name = input("Hello! What is your name?\n")

#     rand_num = rand.randint(1, 20)

#     print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")

#     i = 0
#     num = 0
#     while num != rand_num:
#         num = int(input())
#         i += 1

#         if num < rand_num:
#             print("Your guess is too low.\nTake a guess.")
#         elif num > rand_num:
#             print("Your guess is too high.\nTake a guess.")
#         else:
#             print(f"Good job, {name}! You guessed my number in {i} guesses!")

# guess_num()
        

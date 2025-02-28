import os

# 1 task
print(os.listdir())
print([item for item in os.listdir() if os.path.isfile(item)])
print([item for item in os.listdir() if os.path.isdir(item)])


# 2 task
path = r"C:\Users\User\Desktop\materials\PP\PP2\labs\lab1"
print("Exists the path:", os.access(path, os.F_OK))
print("Access to read the file:", os.access(path, os.R_OK))
print("Access to write the file:", os.access(path, os.W_OK))
print("Check if path can be executed:", os.access(path, os.X_OK))


# 3 task
path_a = input("Enter path: ")
if os.path.exists(path_a):
    print(os.path.basename(path_a))
    print(os.path.dirname(path_a))
else:
    print("does not exist")


# 4 task
file_path = input("Enter the file path: ")
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        summa = sum([1 for item in file.readlines()])
        print("Number of lines: ", summa)


# 5 task
entered_list = list(input("Enter list elements: ").split())
with open(r"lab6\example.txt", "a") as file:
    file.writelines('\n'.join(entered_list))
    print("list entered")
    file.close()


# 6 task
import string
for letter in string.ascii_uppercase:
    with open(f"lab6\\{letter}.txt", "w") as file:
        file.close()


# 7 task
import shutil
shutil.copy("lab6\\example.txt", "lab6\\copy.txt")


# 8 task
path = input("Enter path: ")
if os.path.exists(path):
  os.remove(path)
  print("The file has deleted")
else:
  print("The file does not exist")

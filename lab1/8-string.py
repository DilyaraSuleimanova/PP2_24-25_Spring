# QUOTES INSIDE QUOTES
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')



# LOOP THROUGH STRING
for x in "banana":
    print(x)



# STRING LENGTH
a = "Hello, World!"
print(len(a))



# CHECK STRING
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)



# SLICING
b = "Hello, World!"
print(b[:5])
print(b[2:])
print(b[-5:-2])
print(b[2:5])



# MODIFY STRING
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))



# FORMAT STRING
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)



# ESCAPE CHARACTERS
txt = "\tThey are \"Vikings\" from the north. \nHello!"
print(txt)
import string
import random

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to Password Generator")
no_letters = int(input("How many Letters you want in your Password: "))
no_numbers = int(input("How many Numbers you want in your Password: "))
no_symbol = int(input("How many symbol you want in your Password: "))

password = ""
for i in range(no_letters):
    password += random.choice(letters)

for i in range(no_numbers):
    password += random.choice(numbers)


for i in range(no_symbol):
    password += random.choice(symbols)

password_list = list(password)
random.shuffle(password_list)
password = "".join(password_list)

print(f"Generated Password is {password}")    

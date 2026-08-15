import random

Names = input("Enter the Names Separated by comma: ")
names_list = Names.split(",")
random_name = random.choice(names_list)

print(f"{random_name} will pay the Bill")
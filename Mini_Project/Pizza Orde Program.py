print("----Pizza Order----")
size = input("Size of Pizza(S/M/L): ")
bill = 0

if size == 'S' or size == 's':
    bill += 90
    print("Small Pizza price is 90RS")
elif size == 'M' or size == 'm':
    bill += 170
    print("Medium Pizza is 170RS")
else:
    bill += 260
    print("Large Pizza is 260RS")

add_pepperoni = input("Do you want Pepperoni(Y/N): ")
if add_pepperoni == 'y' or add_pepperoni == 'Y':
    if size == 'S' or size == 's':
        bill += 30
    else:
        bill += 50

extra_cheese = input("Want Extra cheese(Y/N): ")        
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 20
print("Overal Bill is: ", bill)            
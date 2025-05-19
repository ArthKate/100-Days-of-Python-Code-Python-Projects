import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# complex level - Order of characters randomised:
complex_passwd = []


for _ in range(nr_letters):
    complex_passwd.append(random.choice(letters))

# Numbers
for num in range(1, nr_numbers + 1):
    complex_passwd.append(random.choice(numbers))

# Symbols
for symbol in range (1, nr_symbols + 1):
    complex_passwd.append(random.choice(symbols))

# Easy level - Order not randomised:
print(f"Your easy password is: {''.join(complex_passwd)}")


# Hard level - Order of characters randomised:
random.shuffle(complex_passwd)
print(f"your complex password is : {''.join(complex_passwd)}")

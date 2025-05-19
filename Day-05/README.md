# Password Generator

This project is a solution to the **Password Generator** challenge from Day 5 of the 100 Days of Python course. The program generates a random, secure password based on user-defined criteria.

## Features

- **Customizable Password Length**: Users can specify the number of letters, symbols, and numbers in the password.
- **Randomized Order**: The generated password is randomized to enhance security.
- **User-Friendly Input**: The program prompts the user for input, making it easy to customize the password.

## How It Works

1. The user is prompted to input:
  - Number of letters.
  - Number of symbols.
  - Number of numbers.
2. The program generates the specified number of characters from predefined lists:
  - Letters: `a-z`, `A-Z`
  - Symbols: `!@#$%^&*()_+-=[]{}|;:'",.<>?/`
  - Numbers: `0-9`
3. The selected characters are shuffled to create a randomized password.
4. The final password is displayed to the user.

## Example

Input:
```
How many letters would you like in your password? 4
How many symbols would you like? 2
How many numbers would you like? 3
```

Output:
```
Your password is: G7!a2@b5
```

## Key Concepts

- **Random Module**: Used to select random characters and shuffle the password.
- **Lists**: Store letters, symbols, and numbers for easy access.
- **String Manipulation**: Combine and shuffle characters to form the final password.

## How to Run

1. Clone the repository.
2. Navigate to the `Day-05` folder.
3. Run the `password_generator.py` script using Python:
  ```
  python password_generator.py
  ```

## Learning Outcomes

- Practice with Python's `random` module.
- Understand how to manipulate strings and lists.
- Learn to create user-friendly command-line applications.

Enjoy generating secure passwords!
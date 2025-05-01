# Tip Calculator

This is a day-02 project of the **100 Days of Python Code** challenge. It is a simple Python program that helps a group of people calculate the tip to pay on top of the total bill for a pizza order in the restaurant.

## How it works

1. The program prompts the user to input the total bill amount.
2. It then asks for the percentage tip they would like to give (e.g., 10%, 12%, or 15%).
3. The user is prompted to enter the number of people splitting the bill.
4. The program calculates the total amount each person should pay, including their share of the tip.
5. Finally, it displays the amount each person owes, rounded to two decimal places.

## Example

If the total bill is $150.00, the tip percentage is 12%, and there are 5 people splitting the bill:

- Total tip = $150.00 × 12% = $18.00
- Total bill including tip = $150.00 + $18.00 = $168.00
- Amount per person = $168.00 ÷ 5 = $33.60

Each person would pay **$33.60**.

## How to run the program

1. Clone this repository to your local machine.
2. Navigate to the `Day-02` folder.
3. Run the `tip_calculator.py` file using Python:
  ```bash
  python tip_calculator.py
  ```

## Concepts covered

- Basic arithmetic operations in Python.
- Input and output handling.
- String formatting for displaying results.
- Rounding numbers to a specific decimal place.
- Simple user interaction through the console.
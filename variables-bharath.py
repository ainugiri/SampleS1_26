# Restaurant Order System

# Scenario:
# A restaurant wants to store a customer's order using Python data types.

# Task:
# Write a Python program that:

# Store the customer name (string).
name = "bharath"   
# Store ordered items using a list.
items = ["Dosa", "Idli", "Coffee"]
# Store unique item categories using a set.
categories = {"Breakfast", "Beverage"}
# Store price of each item using a dictionary.
prices = {
    "Dosa": 50,
    "Idli": 30,
    "Coffee": 20
}
# Calculate the total bill amount.

print(f"Customer Name: {name}")
print(f"Items Ordered: {items}")
print(f"Categories: {categories}")
total_bill = sum(prices[item] for item in items)
print(f"Total Bill: {total_bill}")
# Example Data

# Items Ordered: ["Dosa", "Idli", "Coffee"]
# Prices:
# Dosa → 50
# Idli → 30
# Coffee → 20

# Expected Output

# Customer Name: Arun
# Items Ordered: ['Dosa', 'Idli', 'Coffee']
# Categories: {'Breakfast', 'Beverage'}
# Total Bill: 100

# Concepts Used

# str

# list

# set

# dict

# int
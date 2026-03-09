# Student Information System

# Scenario:
# A school wants to store information about a student using different Python data types.

# Task:
# Write a Python program that:

# Stores the following details:

# Student Name (string)
name = "Vishwa"
# Age (integer)
age = 20
# Marks in 3 subjects (list)
marks = [75,95,85]
# Passed or Failed (boolean)
pass_status = True
# Store all details inside a dictionary.
student = {
    "name":name,
    "age":age,
    "marks":marks,
    "result": pass_status
}
print(student)
# Calculate the average marks.
avg_mark = sum(marks)/len(marks)

# Display all the student details and the average.

print(f"Student Name: {student['name']}")
print(f"Student Age: {student['age']}")
print(f"Student Mark: {student['marks']}")
print(f"Student Average Score: {avg_mark}")
print(f"Pass: {student['result']}")


# Expected Output Example

# Student Name: Ravi
# Age: 14
# Marks: [78, 85, 90]
# Average Marks: 84.33
# Result: True


# ***************************************
# Library Book Management

# Scenario:
# A library wants to store information about books and check if a book is available.

# Task

# Write a Python program that:

# Stores the library name (string).
library_name="city central library"

# Stores a list of books available.
books=("tamil","english","maths","science")

# Stores book availability status using a dictionary.
book_status={
    "Tamil":True,
    "English":False,
    "Maths":True,
    "Science":False,
}
print("library name:",library_name)
print("books_status:",books)
print("books availability status")
 
def calc(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

while True:
    inp1 = int(input("Enter the first number: "))
    inp2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    result = calc(inp1, inp2, operation)
    print("The result is:", result)

    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        print("Calculator stopped.")
        break

while True:
    amount=int(input("enter the amount:"))
    if(amount>=5000):
        discount=(25/100*amount)
    elif(amount>=3000):
        discount=(15/100*amount)
    elif(amount>=1000):
        discount=(10/100*amount)
    else:
        discount=0
    print("original amount:",amount)
    print("discount amount:",discount)
    final=amount-discount
    print("final payable amount:",final)


balance = float(input("Enter your account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
if withdraw_amount > balance:
    print("Error: Insufficient balance.")
elif withdraw_amount > 20000:
    print("Error: Withdrawal limit per transaction is ₹20,000.")
else:
    balance = balance - withdraw_amount
    print("Withdrawal successful.")
    print("Remaining balance:", balance)

units = int(input("Enter units: "))
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 100*2 + (units-100)*4
else:
    bill = 100*2 + 100*4 + (units-200)*6

if bill > 1000:
    bill += bill * 0.05

print("Final Electricity Bill: ₹", bill)


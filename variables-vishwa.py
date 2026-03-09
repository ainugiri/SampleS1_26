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


# Arithmetic Operator
# Addition +
# Subtraction -
# Multiplication *
# division /
# Modulus (Sending the remainder) = %
# Power **

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def remainderofdiv(x,y):
    return x%y
def power(x,y):
    return x**y
def floordivisor(x,y):
    return x//y

inp1 = int(input("Enter a value : "))
inp2 = int(input("Enter a value : "))
print(f"{inp1} to the power of {inp2} is {power(inp1,inp2)}")
print(f"While dividing {inp1} by {inp2}, we got floor divisor value {floordivisor(inp1,inp2)}")
print(f"While dividing {inp1} by {inp2}, we got remainder value {remainderofdiv(inp1,inp2)}")




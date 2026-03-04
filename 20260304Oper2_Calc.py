# function (x,y,op)
# x - value : 25
# y = value : 10
# op = + - / * // ** %
# return + 32, - 15, 2.5, 250, 2, 250000000000, 5

def calc(x,y,op):
    if op == "+":
        return x+y


inp1 = int(input("Enter the first number : "))
inp2 = int(input("Enter the second number : "))
operation = input("Enter the operation need to be done : ")
result = calc(inp1, inp2, operation)
print("The result is ", result)


# 10 + 25 = 35
# 35 + 5= 40 +10 = 50 + 25 =75 + 11 = 86 + 12 =98 q result 98
mark1 = 'A'
print(mark1, type(mark1))
mark2 = 90
print(mark2, type(mark2))

# notepad write
# paper write 
# 1. onion , 
# 2. tomato
# 3. potato
# order
# indexing 

# collection of data
# super market
# unordered - trollay

# bill 
# scanner - barcode & get price
# key and value pair

# list
# 1. ordered
# 2. mutable
# 3. indexed
marks = [90, 80, 70, 60]
print(marks, type(marks))

# access through index
# index starts with 0
print(marks[0])
print(marks[1])

# mutable - change the value
marks[0] = 95
print(marks)

marks.append(50) # add the value at the end of the list
marks.insert(2,88) # add the value at the specific index
print(marks)

marks.pop() # remove the last value
print(marks)
marks.pop(2) # remove the value at the specific index
print(marks)

# now i am billing it. the item in the bill-> not changeable
items = ('onion', 'tomato', 'potato')
print(items)
# items[0] = 'Gold Coin' # error - tuple is immutable
l1 = list(items) # convert tuple to list
l1[0] = 'Gold Coin' # change the value in the list
items = tuple(l1) # convert list back to tuple
print(items)
# items.append('carrot') # error - tuple is immutable
# items.pop() # error - tuple is immutable
# items.insert(1, 'carrot') # error - tuple is immutable
items = tuple() # empty tuple
print(items)


cprogramming = {'Bharath', 'Ravi', 'Suresh', 'Vishwa'}
pythonprogramming = {'Bharath', 'Mohammed', 'James', 'Vishwa', 'Anusha'}
javaprogramming = {'Bharath', 'Vishwa', 'Rekha','Michael', 'Elizabeth'}

allskill_persons = cprogramming.intersection(pythonprogramming).intersection(javaprogramming)
print(allskill_persons)

atleastone_skill_persons = cprogramming.union(pythonprogramming).union(javaprogramming)
print(atleastone_skill_persons)

print(cprogramming)

cprogramming.add('Anusha') # add a value to the set
print(cprogramming)

l1 = ['Girish', 'Suresh', 'Prasad']
cprogramming.update(l1) # add multiple values to the set
print(cprogramming)
cprogramming.add('Bharath')
print(cprogramming) # set does not allow duplicate values

cprogramming.remove('Girish') # remove a value from the set
print(cprogramming)
# cprogramming.remove('Girish') # remove a value from the set
# print(cprogramming)

cprogramming.discard('Anusha') # remove a value from the set
print(cprogramming)
cprogramming.discard('Anusha') # remove a value from the set
print(cprogramming)

cprogramming.pop()
print(cprogramming)

cprogramming.clear() # remove all values from the set
print(cprogramming)
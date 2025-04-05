#DATA STRUCTURES

#In Python, each object in a list can be of a different type
letters = ['a', 'b', 'c']
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
print(combined)
numbers = list(range(20))
chars = list("Hello World")
print(chars)
print("The second item in the letters list is: " + letters[1])

#We can modify an individual item by accessing it using the square bracket
letters[0] = 'A'
print(letters)

#We can print a part of the list using this syntax(it won't change the original list) (the first arg is beginning, second arg is length): 
print(letters[0:2])
print(letters)

#We can select even numbers using this syntax
evenNumbers = list(range(20))
print(evenNumbers[::2])
#If we change the step (2) to -1, we will get the list in reverse
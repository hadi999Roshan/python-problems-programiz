# #Algorithm to find the greatest number between 3 numbers:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if ( num1 >= num2 ) and ( num1 >= num3 ):
    greatest_num = num1
elif ( num2 >= num1 ) and (num2 >= num3):
    greatest_num = num2
else:
    greatest_num = num3

print(f"The greatest number among the 3 input numbers is: { greatest_num }")

#Algorithm to find all of the prime numbers between two numbers:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
for num in range( num1, num2 + 1 ):
    if num > 1:
        for i in range( 2, num ):
            if ( num % i ) == 0:
                break
            else:
                print(num)
#THIS PROGRAM PRINTS EVERY NUMBER MULTIPLE TIMES! WHY IS THIS THE CASE?!

#Algorithm to print the multiplication table of a number
input_num = int(input("Enter the number you want to see the multiplication table of: "))
for i in range ( 1, 11 ):
    print(f"{ input_num } * { i } = { input_num * i }")

#Algorithm to find the sum of numbers up to an input number
input_num = int(input("Enter a positive number: "))
if input_num <= 0:
    input_num = int(input("The number you have entered is not valid. Please enter a positive number: "))

sum = 0
while (input_num > 0):
    sum += input_num
    input_num -= 1
print(f"The sum is: { sum }")

#Algorithm to find numbers divisible by 13
my_list = [26, 55, 100, 221, 500]
result = list(filter(lambda x: (x % 13 == 0), my_list))
print(f"Numbers divisible by 13 are {result}")

#Algorithm to find the ASCII value for a character
c = str(input("Enter the character that you want to find the value of: "))
print("The ASCII value of '" + c + "' is", ord(c))
#Here we have used ord() function to convert a character to an integer 
#(ASCII value). This function returns the Unicode code point of that 
#character.

#Algorithm to find the LCM of two numbers:
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))

#
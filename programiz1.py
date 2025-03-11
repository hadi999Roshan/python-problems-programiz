#Algorithm to find the square root of a positive number
pos_num = 16
num_sqrt = pos_num ** 0.5
print(f"The square root of { pos_num } is { num_sqrt }")

#Algorithm to solve the quadratic equation ax**2 + bx + c = 0
import cmath
num_a = 1
num_b = 5
num_c = 6
d = (num_b**2) - (4*num_a*num_c)
sol1 = (-num_b-cmath.sqrt(d))/(2*num_a)
sol2 = (-num_b+cmath.sqrt(d))/(2*num_a)
print(f"The two solutions are { sol1 } and { sol2 }")

#Algorithm to generate a random number between 0 and 9
import random
print("This program generates a random number between 0 and 9")
print(random.randint(0,9))

#Algorithm to convert a distance in kilometers to miles
distance_kilo = float(input("Enter a distance in kilometers: "))
conversion_factor = 0.621371
distance_mile = distance_kilo * conversion_factor
print(f"{ distance_kilo } kilometers is { distance_mile } miles.")

#Algorithm to detect if a number is positive, negative, or zero
input_num = float(input("Enter a number: "))
if input_num > 0:
    print(f"{ input_num } is a positive number.")
elif input_num == 0:
    print(f"{ input_num } is zero.")
else:
    print(f"{ input_num } is a negative number.")
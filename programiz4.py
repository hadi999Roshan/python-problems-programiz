# Python program to shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])

#Algorithm to print the calendar for an input month from the user
import calendar
input_year = int(input("Enter the year that you want to see the calendar for: "))
input_month = int(input("Enter the month that you want to see the calendar for: "))
print(calendar.month(input_year, input_month))

#Algorithm to find the sum of natural numbers using recursion
# Python program to find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

num = 16

print("The sum is",recur_sum(num))

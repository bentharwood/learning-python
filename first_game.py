import random
import math

lower = int(input("Enter Lower Bound: "))
upper = int(input("Enter Upper Bound: "))

x = random.randint(lower, upper)

print(f"\n\tYou've only {round(math.log(upper - lower +1, 2))} chances to guess the number")
count = 0

while count < math.log(upper - lower +1, 2):
  count += 1

  guess = int(input("Guess a number:"))

  if(guess == x):
    print(f"Congratulations you did it in {count} tries")
    break
  elif(guess < x):
    print("You guessed too small!")
  elif(guess > x):
    print("You guessed too high!")
if(count >= math.log(upper - lower +1, 2)):
  print(f"\nThe number is {x}")
  print(f"\tBetter luck next time!")

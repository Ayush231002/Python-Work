import random
import math
#user Input 
lower = int(input("Enter Lower bound:-"))
upper = int(input("Enter Upper bound:-"))

#random number generator
x = random.randint(lower,upper)
print("\n\tYou've only",
      round(math.log(upper -lower+1,2)),
      "chances to guess the number\n")
count = 0
while count < math.log(upper-lower +1,2):
    count+=1

    guess=int(input("Guess a number:-"))

    if x == guess:
        print("Congratulations ",count,"try")

        break
    elif x > guess:
        print("You guessed to small")
    elif x < guess:
        print("You guessed to large")

if count >= math.log(upper - lower +1,2):
    print("\nThe number is %d"%x)
    print("\tBetter Luck Next time")            


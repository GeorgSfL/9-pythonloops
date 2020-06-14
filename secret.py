"""import random

secret = random.randint(1, 100) #1 und 100 sind inkludiert!

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == secret:
        print("OK")
        break
    elif guess < secret:
        print("too small")
    else:
        print("too big")
"""

import random

secret = random.randint(1, 100) #1 und 100 sind inkludiert!

for x in range(10):
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == secret:
        print("OK")
        break
    elif guess < secret:
        print("too small")
    else:
        print("too big")
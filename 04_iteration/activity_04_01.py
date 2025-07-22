"""activity 04.01"""

secret = 7
max_tries = 10
guess = int(input("Guess the number: "))
count = 1
while guess != secret and count < max_tries:
    if guess < secret:
        print("The secret number is greater than", guess)
    else:
        print("The secret number is less than", guess)
    guess = int(input("Try again: "))
    count += 1

if guess == secret:
    print("Correct! It took you", count, "tries")
else:
    print("You ran out of tries :-(")

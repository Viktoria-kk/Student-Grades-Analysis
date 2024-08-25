from random import *

print("Welcome to the Simple Multiplication Quiz! "
      "\nYou will be given 5 multiplication problems to solve.\n")

score = 0
for n in range (1,6):
    while True:
        try:
            a, b = randint(1, 10), randint(1, 10)
            print(f"problem {n}: What is {a} x {b}?")
            user_input = int(input("Your answer: "))

            if user_input == a * b:
                print("Correct!\n")
                score += 1
                break
            else:
                print(f"Incorrect! The correct answer was {a * b}\n")
                break
        except ValueError:
            print("Please enter a number!\n")

if score <= 3:
    print(f"\nYou scored {score} out of {n}. You need to practice more!")
else:
    print(f"\nYou scored {score} out of {n}. Well done!")
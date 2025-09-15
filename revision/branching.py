value = 20

print("Welcome to the number guessing game!")
guess = int(input(f"Enter a number between 1 and 50: "))

if guess == value:
    print("Correct!")
elif guess < value:
    print("Too low.")
else:
    print("Too high!")


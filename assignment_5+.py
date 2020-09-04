# Don't change these lines
number = int(input("Find the square root of integer: "))
guess = int(input("Initial guess: "))
tolerance = float(input("What tolerance: "))

count = 0 
previous = 0


while abs(previous - guess) > tolerance:
    previous = guess
    quotient = number/guess
    guess = (quotient+guess)/2
    count = count + 1

# Don't change these lines
print("Square root of", number, "is", round(guess, 4))
print("Took", count, "reps to get it to tolerance")

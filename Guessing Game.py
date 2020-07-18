# Guessing game using While loop
guess_count = 0
guess_limit = 3
target = 11
# 1
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    if guess == target:
        print("You Won!")
        break
    else:
        guess_count += 1
else:
    print("Sorry, You Failed!")

"""
# 2
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1 
    if guess == target: 
        print("You Won!")
        break
else: 
    print("Sorry, You Failed!")

"""

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
"""BUG:
toss is always gonna be either 0 or 1, while the initial input requires either 'heads' or 'tails'
"""
if toss == guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess = input()
    """BUG:
    No checking if the input is valid.
    Same problem as before.
    toss doesn't get a new value.
    """
    if toss == guess:
        print("You got it!")
    else:
        print("Nope! Still fucking awful!")
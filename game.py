from random import randint

print "Hello!, what's your name?"
username = raw_input("(type your name): ")
print username,", I'm thinking of a number between 1 and 100."

print "Try to guess my number."
secret_number = randint(1, 100)
print secret_number
guess = None

number_of_guesses = 0

while guess is not secret_number:
    number_of_guesses = number_of_guesses + 1
    guess = int(raw_input("Your guess? "))
    if guess < secret_number:
        print "Your guess is too low, try again."
    elif guess > secret_number:
        print "Your guess is too high, try again."
    
print "Well done, %s! You found my number in %s tries." % (username, number_of_guesses)
# "! You found my number in ", guesses,"guesses"
    
import random


def get_valid_int(message):
    while True:
        number = input(message)

        if number.isdigit():
            return int(number)

        print("enter a number.")


def play_user_rounds(min, max, target):
    guesses = 0

    while True:
        guess = get_valid_int("enter your guess: ")
        guesses = guesses + 1

        if guess == target:
            print("you got it.")
            return guesses

        elif guess < target:
            print("too low.")

        else:
            print("too high.")


def play_cmp_rounds(min, max, target):
    guesses = 0
    low = min
    high = max

    while True:
        guess = random.randint(low, high)
        guesses = guesses + 1

        print(f"computer guessed {guess}")

        if guess == target:
            print("the computer got it.")
            return guesses

        elif guess < target:
            low = guess + 1

        else:
            high = guess - 1


def print_outcome(user_guesses, comp_guesses):
    print(f"you used {user_guesses} guesses.")
    print(f"the computer used {comp_guesses} guesses.")

    if user_guesses < comp_guesses:
        print("you used fewer guesses.")
    elif comp_guesses < user_guesses:
        print("the computer used fewer guesses!")
    else:
        print("you tied!")


def play_again():
    answer = input("play again? (yes/no): ")

    if answer.lower() == "yes":
        return True
    else:
        return False


min = get_valid_int("enter the minimum number: ")
max = get_valid_int("enter the maximum number: ")

target = random.randint(min, max)

while True:

    user_guesses = play_user_rounds(min, max, target)

    comp_guesses = play_cmp_rounds(min, max, target)

    print_outcome(user_guesses, comp_guesses)

    if play_again():
        target = random.randint(min, max)
    else:
        print("have a terrible day!")
        break

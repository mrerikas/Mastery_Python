from random import randint


def guessNumber():

    player_name = input("Please type your nickname: ")
    number_of_guesses = 0
    secret_number = randint(1, 11)
    print(f"Hello {player_name}, now I generate number from 1 to 10!")

    while number_of_guesses < 5:
        guess = int(input(f"{player_name} choose number from 1 to 10: "))
        number_of_guesses += 1
        if guess < secret_number:
            print('Your number is to low!')
        elif guess > secret_number:
            print('Your number is to high!')
        elif guess == secret_number:
            break

    if guess == secret_number:
        print(f"Good job {player_name}, you guessed number from {number_of_guesses} tries!")
    else:
        print(f"You haven't guessed number. Number was {secret_number}.")

    again = input(
        "Do you want to repeat? If yes, type 'y', overwhise 'n' to end the game: ").lower()
    if again == 'y':
        return guessNumber()
    elif again == 'n':
        return print('I realy enjoyed to play with you, hope to see you soon!')
    else:
        return print('I dont understand your command..')


guessNumber()

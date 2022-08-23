#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random

chosen_word = random.choice(word_list)
# print(chosen_word)
# print(guess)

spaces = ["X"] * len(chosen_word)
#show all the available spaces by printing X


def get_letter_position(guess, chosen_word, spaces):
    index = -2
    # loop to iterate through the word for every position the letter exists, -2 is the best place to start the iteration
    while index != -1:
        if guess in chosen_word:
            index = chosen_word.find(guess)
            removed_character = '*'
            chosen_word = chosen_word[:index] + removed_character + chosen_word[
                index + 1:]
            spaces[index] = guess
        else:
            index = -1
    return (chosen_word, spaces)


def win_check():
    for i in range(0, len(spaces)):
        if spaces[i] == 'X':
            return -1
    return 1


num_turns = len(chosen_word)
for i in range(-1, num_turns):
    print("Welcome, here is the hidden word " + str(spaces))
    print('\nYou have ' + str(num_turns - i) + ' turns to try.')
    guess = str(input("\nPlease pick a letter ").lower())

    if guess in chosen_word:
        word, spaces = get_letter_position(guess, chosen_word, spaces)
        print("Correct => " + str(spaces))
    else:
        print('Sorry that letter is not in the word.')

    if win_check() == 1:
        print('Congratulations you won')
        break

    print('You have ' + str(num_turns - i) + ' turns left.')
    print()

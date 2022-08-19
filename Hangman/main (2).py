#Step 1
# word_list = ["aardvark", "baboon", "camel"]
from hangman_words import word_list
from hangman_art import stages 
from hangman_art import logo
import random

end_of_game = False
if end_of_game == True:
  exit()
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
# print("Psst, hint - the chosen word is" + chosen_word)
# print(guess)

#Set 'lives' to equal 6.
livesy = 6
num_turns = len(chosen_word)

spaces = ["X"] * len(chosen_word)
#show all the available spaces by printing X



#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
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
                          
    return 1  #Player has won

def lives_rem():
    if livesy == 0: 
      print("\nGame Over, you lost all your lives")
      end_of_game == True,
     



for i in range(-1, num_turns):
    print("Welcome, here is the hidden word " + str(spaces))
    print('\nYou have ' + str(num_turns) + ' letters to fill.')
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = str(input("\nPlease pick a letter ").lower())

    if guess in chosen_word:
        lives, word,  = get_letter_position(guess, chosen_word, spaces)
        print("Correct => " + str(spaces))
        words_left = len(spaces)-1
        print('You have ' + str(num_turns - i) + ' letters left.')
    else:
        livesy = livesy - 1
        lives_rem()
        print('Sorry that letter is not in the word.')
    
    print("You have " + str(livesy) + " lives remaining.")
    lives_rem()
    occurrence = {item: spaces.count(item) for item in spaces}
    words_left = occurrence.get('X')
    # words_left = chosen_word.count['X'] 
    print('You have ' + str(words_left) + ' letters left.')
    

    if win_check() == 1:
        print('Congratulations you won')
        break



    # print('You have ' + str(num_turns - i) + ' letters left.')
    # print()
    # print(len(chosen_word))

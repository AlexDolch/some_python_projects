import random
import string

from wordlist import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else " - " for letter in word]
        print("current word: ", "".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1

        elif user_letter in used_letters:
            print("U have already used that Character!")

        else:
            print("Invalid Character")

    if lives == 0:
        print("You died. The word was", word,"you N00B!!")
    else:
        print("You guessed the word", word, "!!")

hangman()
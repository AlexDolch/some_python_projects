
import random
import sys
from termcolor import colored


def random_word():
    word_list = open(r"C:\Users\AlexD\Desktop\Coding\Small Projects\Wordle_Clone\wordle_wordlist.txt").read().splitlines()
    return random.choice(word_list).lower()


word = random_word()

for attempt in range(1, 7):
    guess = input("\n Ur guess: ").lower()
    for i in range (min(len(guess), 5)):
        if guess[i] == word[i]:
            print(colored(guess[i], "green"), end="")
        elif guess[i] in word:
            print(colored(guess[i], "yellow"), end="")
        else:
            print(guess[i], end="")
        
        if guess == word:
            print("Congrats! {guess} was the word, u took {attempt} attempts.")




#print("        - Let's play wordle! - ")
#print(" - Type a 5 letter word and hit enter - \n")
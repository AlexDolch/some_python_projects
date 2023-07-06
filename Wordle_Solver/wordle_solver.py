
import numpy as np
import string

word_list = open("wordle_wordlist.txt").read().splitlines()


def wrongLetters(result, guess):
    wrong_letters = []
    for char in range(0, 5):
        if result[char] == "w":
            wrong_letters.append(guess[char])
    return wrong_letters


def misplacedLetters(result, guess):
    misplaced_letters = []
    for char in range(0, 5):
        if result[char] == "y":
            misplaced_letters.append([guess[char], char])
    return misplaced_letters


def correctLetters(result, guess):
    correct_letters = []
    for char in range(0,5):
        if result[char] == "g":
            correct_letters.append([guess[char], char])
    return correct_letters


def word_remover(result, guess, word_list):
    wrong_letters = wrongLetters(result, guess)
    misplaced_letters = misplacedLetters(result, guess)
    correct_letters = correctLetters(result, guess)
    good_letters = []
    
    for g in correct_letters:
        good_letters.append(g[0])
    for y in misplaced_letters:
        good_letters.append(g[0])
    
    acceptable_words1 = []
    for w in word_list:
        check = 0
        for b in wrong_letters:
            if b in w:
                if b in good_letters:
                    pass
                else:
                    check = 1
                    break
        if check == 0:
            acceptable_words1.append(w)
    #print(acceptable_words1)

    acceptable_words2 = []
    for w in acceptable_words1:
        check = 0
        for g in correct_letters:
            if w[g[1]] != g[0]:
                check = 1
                break
        if check == 0:
            acceptable_words2.append(w)
    #print(acceptable_words2)
    
    acceptable_words3 = []
    for w in acceptable_words2:
        check = 0
        for p in misplaced_letters:
            if w[p[1]] == p[0]:
                check = 1
                break
        if check == 0:
            acceptable_words3.append(w)
    #print(acceptable_words3)
    
    acceptable_words4 = []
    for w in acceptable_words3:
        check = 0
        for g in good_letters:
            if g not in w:
                check = 1
                break
        if check == 0:
            acceptable_words4.append(w)
    #print(acceptable_words4)

    acceptable_words5 = []
    for w in acceptable_words4:
        check = 0
        for b in wrong_letters:
            if b in good_letters:
                if w.count(b) != good_letters.count(b):
                    check = 1
                    break
        if check == 0:
            acceptable_words5.append(w)
    
    return acceptable_words5


def letterFreq(word_list):
    arr = {}
    for letter in string.ascii_lowercase:
        freq = [0, 0, 0, 0, 0]
        for char in range(0, 5):
            for word in word_list:
                if word[char] == letter:
                    freq[char] += 1
        arr.update({letter: freq})
    return arr


def wordScore(word_list, frequencies):
    words = {}
    max_freq = [0, 0, 0, 0, 0]
    for c in frequencies:
        for char in range(0, 5):
            if max_freq[char] < frequencies[c][char]:
                max_freq[char] = frequencies[c][char]
    for word in word_list:
        score = 1
        for char in range(0, 5):
            c = word[char]
            score *= 1 + (frequencies[c][char] - max_freq[char]) ** 2
        words.update({word: score})
        score += np.random.uniform(0, 1)
    return words


def bestWord(word_list, frequencies):
    max_score = 1_000_000_000
    best_word = "words"
    scores = wordScore(word_list, frequencies)
    for word in word_list:
        if scores[word] < max_score:
            max_score = scores[word]
            best_word = word
    return best_word


def wordleSolver(word_list):
    print("Welcome to Wordle Solver")
    print("The suggested starting word is: ", bestWord(word_list, letterFreq(word_list)))
    print("Enter your first guess:")
    guess = input()
    print("Enter your first result:")
    result = input()
    counter = 1
    while result != "ggggg" and counter < 6:
        word_list = word_remover(result, guess, word_list)
        print(word_list)
        if len(word_list) == 0:
            break
        suggestion = bestWord(word_list, letterFreq(word_list))
        print("The suggested word is:", suggestion)
        print("Enter your next guess:")
        guess = input()
        print("Enter your new result:")
        result = input()
        counter += 1
    if len(word_list) == 0:
        print("Oh no! You made a mistake entering one of your results. Please try again.")
    elif counter == 6 and result != "ggggg":
        print("Number of guesses exceeded, sorry we failed!")
    else:
        print("Congratulations! We solved today's Wordle in", counter, "guesses.")


wordleSolver(word_list)


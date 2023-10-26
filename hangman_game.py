import string
from words import words
import random
import os


def get_word_from_words(words_array):
    word: str = random.choice(words_array)

    while "-" in word or len(word) < 3:
        word = random.choice(words_array)
    return word.upper()


def get_word():
    word = ""
    while len(word) < 3 and "-" not in word and " " not in word and not has_numbers(word):
        word = input("Enter your word (no spaces and numbers):").upper()
    return word


def set_tries(x: int) -> int:
    return x


def play_default_hangman(one=True):
    play_hangman(tries=6, one=one)


def image(num_tries: int, errors: int):
    ret = ""

    if errors == 0:
        ret = " _______\n | /   |\n |/\n |\n |\n/|\\"
    elif errors == 1:
        ret = " _______\n | /   |\n |/    O\n |\n |\n/|\\"
    elif errors == 2:
        ret = " _______\n | /   |\n |/    O\n |     |\n |\n/|\\"
    elif errors == 3:
        ret = " _______\n | /   |\n |/    O\n |     |\n |    /\n/|\\"
    elif errors == 4:
        ret = " _______\n | /   |\n |/    O\n |     |\n |    / \\\n/|\\"
    elif errors == 5:
        ret = " _______\n | /   |\n |/    O\n |    /|\n |    / \\\n/|\\"
    elif errors == 6:
        ret = " _______\n | /   |\n |/    O\n |    /|\\\n |    / \\\n/|\\"
    elif errors > 6:
        ret = " _______\n | /   |   o\n |/        ^\n |         ^\n |    /|\\\n/|\\   / \\  o"

    return f"{ret}\n   {num_tries - errors} tries left"


def play_hangman(tries=6, one=True):
    if one:
        word = get_word_from_words(words)
    else:
        word = get_word()
        os.system("cls")
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    num_wrong_guesses = 0
    num_allowed_guesses = tries
    win = False
    forced_end = False

    while len(word_letter) > 0 and num_wrong_guesses < num_allowed_guesses:
        # image
        print(image(tries, num_wrong_guesses))

        # used letters
        print("Used letters: " + " ".join(used_letters))

        # print word's image
        print("Current word:", " ".join(i if i in used_letters else "-" for i in word))

        letter = input("Guess the letter: ").upper()

        if letter in alphabet - used_letters:
            if letter in word_letter:
                word_letter.remove(letter)
            else:
                print(f"Letter {letter} not in the word.")
                num_wrong_guesses += 1

            used_letters.add(letter)
        elif letter in used_letters:
            print("You have used this letter already")
        elif letter == "lms".upper() or letter == "let me see".upper():
            print(word)
        elif letter == "reset".upper():
            num_wrong_guesses = 0
        elif letter == "set".upper():
            new_tries = set_tries(int(input("Tries: ")))
            num_wrong_guesses = tries - new_tries if tries - new_tries > 0 else 0
        elif letter == "xna".upper():
            forced_end = True
            break
        elif letter == word:
            for i in word_letter: used_letters.add(i)
            word_letter = []
        else:
            print("Enter a valid character")

        if len(word_letter) == 0:
            win = True

    if win:
        print(" ".join(i if i in used_letters else "-" for i in word))
        guess_variable = "guess" if num_wrong_guesses == 1 else "guesses"
        print(f"Congrats u won!!!\nYou correctly guessed the word {word} "
              f"with {num_wrong_guesses} wrong {guess_variable}.")

    else:
        if not forced_end:
            print(image(tries, num_wrong_guesses))
            print(f"DEAD!!! U lost!!!\nThe word was: {word}")
        else:
            more_than_6 = 7
            print(image(more_than_6, more_than_6))
            print("Forced end of the program!!!")


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

continue_hangman = ""


if __name__ == "__main__":
    prompt = ""
    while prompt != "1" and prompt != "2":
        prompt = input("Enter the number of players (1 | 2): ")
    while continue_hangman != "xna" and continue_hangman.lower() != "no":
        if "1" in prompt:
            play_default_hangman(one=True)
        else:
            play_default_hangman(one=False)
        # play_hangman(10)
        continue_hangman = input("\nDo you want to continue? -->:")
    print("End of the game! \nHave a great day!")

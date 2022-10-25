from random import choice
import string
alphabet = list(string.ascii_lowercase)
#list of words

keyword = ["apple","blueberry","banana","avocado","tomato"]
#selecting a random word from the list of words
selected_word = choice(keyword)
#listing out the word and then making a string with the same number of blanks
listed_word = list(selected_word)
underscores = list("_" * len(selected_word))


#masking the word with underscores
def replace_with_underscores():
    for i in listed_word:
        i ="_"
    print("".join(underscores))

def user_guess():
    blanks = "".join(underscores)
    print(f"The word is: {blanks}")
    guesses = 5
    while guesses <= 5 :
        guess = input("what letter would you like to guess? \n")
        if guess not in listed_word:
            print("whoops!")
            guesses -= 1
            print(f"you have {guesses + 1 } guesses left!")
        user_input = guess
        #using enumerate() to iterate over a list's indeces
        for index, char in enumerate(listed_word):
            if char == guess:
                underscores[index] = guess
        else:
            if "_" not in underscores:
                success_word = "".join(underscores)
                print(f"Congratulations! The word is {success_word}!")
                break
        print("".join(underscores))
        if guesses < 0:
            print(f"game over! The word was {selected_word}.")
            break
user_guess()

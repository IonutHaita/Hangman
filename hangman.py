import random

placeholder = []
word_list = ["door", "cauliflower", "baboon"]
index = -1
game_over = False
didnt_guess = 0
guesses = 0

chosen_word = random.choice(word_list)

print(chosen_word)
for letter in chosen_word:
    placeholder.append("_")
print(placeholder)

while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()
    print(guess)
    guessed = False
    index = -1
    for letter in chosen_word:
        index += 1
        if letter == guess:
            guesses += 1
            placeholder[index] = letter
            guessed = True

    for char in placeholder:
        display += char
    print(display)
    if not guessed:
        didnt_guess += 1

    if len(chosen_word) == guesses:
        game_over = True
        print("Well done!")
    if didnt_guess == 7:
        game_over = True
        print("Sorry, you failed to guess the word!\n Your character has been hanged")

    
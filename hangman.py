import random

placeholder = []
word_list = ["door", "cauliflower", "baboon"]
game_over = False
didnt_guess = 0
guesses = 0
winner = ['''
          \ O /
            |
            |
           / \ ''']
stage =  ['''
          +----+
          |    |
               |
               |
               |
               |
        ==========
          ''','''
          +----+
          |    |
          O    |
               |
               |
               |
        ==========
        ''','''
          +----+
          |    |
          O    |
         /     |
               |
               |
        ==========
        ''','''
          +----+
          |    |
          O    |
         / \   |
               |
               |
        ==========
        ''','''
          +----+
          |    |
          O    |
         /|\   |
               |
               |
        ==========
        ''','''
          +----+
          |    |
          O    |
         /|\   |
          |    |
               |
        ==========
        ''','''
          +----+
          |    |
          O    |
         /|\   |
          |    |
         /     |
        ==========
        ''','''
          +----+
          |    |
          O    |
         /|\   |
          |    |
         / \   |
        ==========
        '''
          ]
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
    index = 0
    for letter in chosen_word:
        if letter == guess:
            guesses += 1
            placeholder[index] = letter
            guessed = True
        index += 1

    for char in placeholder:
        display += char
    print(display)
    if not guessed:
        didnt_guess += 1

    if "_" not in display:
        game_over = True
        print("Well done!")
        print(winner[0])
    if not guessed:
        print(stage[didnt_guess])
    if didnt_guess == 0:
        game_over = True
        print("Sorry, you failed to guess the word!\nYour character has been hanged")

    
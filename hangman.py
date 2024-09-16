import random

placeholder = []
word_list = ["door", "cauliflower", "baboon"]
game_over = False
didnt_guess = -1
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
    index = 0
    for letter in chosen_word:
        if letter == guess:
            guesses += 1
            placeholder[index] = letter
        index += 1

    for char in placeholder:
        display += char
    print(display)

    if guess not in chosen_word:
        didnt_guess += 1
        print(stage[didnt_guess])

    if "_" not in display:
        game_over = True
        print("Well done!")
        print(winner[0])

    if didnt_guess == 0:
        game_over = True
        print("Sorry, you failed to guess the word!\nYour character has been hanged")

    
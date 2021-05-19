from random import choice

print(*"HANGMAN")

while True:
    user_choice = input('Type "play" to play the game, "exit" to quit: ')
    if user_choice == 'exit':
        break
    elif user_choice != 'play':
        continue

    chosen = list(choice(["python", "java", "kotlin", "javascript"]))
    state = list('-' * len(chosen))

    lives = 8
    past_guesses = set()

    while lives > 0:
        print()
        print(''.join(state))
        guess = input("Input a letter: ")

        if len(guess) != 1:
            print("You should input a single letter")
        elif not guess.islower():
            print("Please enter a lowercase English letter")
        elif guess in past_guesses:
            print("You've already guessed this letter")
        else:
            past_guesses.update(guess)

            if guess not in chosen:
                print("That letter doesn't appear in the word")
                lives -= 1
            else:
                state = [new if new == guess else old
                         for new, old in zip(chosen, state)]

                if state == chosen:
                    break

    if lives > 0:
        print(f"You guessed the word {''.join(state)}!"
              "You survived!", sep='\n', end='\n\n')
    else:
        print("You lost!", end='\n\n')

from random import choice

print(*"HANGMAN")

chosen = list(choice(['python', 'java', 'kotlin', 'javascript']))
state = list('-' * len(chosen))

for _ in range(8):
    print()
    print(''.join(state))
    guess = input("Input a letter: ")
    if guess not in chosen:
        print("That letter doesn't appear in the word")
    else:
        state = [new if new == guess else old
                 for new, old in zip(chosen, state)]

print("""\nThanks for playing!
We'll see how well you did in the next stage""")

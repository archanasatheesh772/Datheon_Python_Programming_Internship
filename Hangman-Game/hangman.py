
import random

# Step 1: Word list
words = [
    "PYTHON", "COMPUTER", "PROGRAM",
    "DEVELOPER", "KEYBOARD", "NETWORK",
    "DATABASE", "SOFTWARE"
]

# Step 2: Select a random word
secret_word = random.choice(words)

# Step 3: Initialize variables
guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

# Step 4: Hangman ASCII stages
stages = [
    """
     _______
     |     |
     |
     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    /
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    / \\
     |
    _|_
    """
]

# Step 5: Display the hidden word
def display_word():
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

# Step 6: Main game
print("\n==============================")
print("       WELCOME TO HANGMAN")
print("==============================")

while wrong_guesses < max_attempts:

    print(stages[wrong_guesses])

    print("Word:", display_word())
    print("Wrong attempts:", wrong_guesses, "/", max_attempts)

    if all(letter in guessed_letters for letter in secret_word):
        break

    guess = input("\nGuess a letter: ").upper().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Step 7: Final result
if all(letter in guessed_letters for letter in secret_word):

    print("\n==============================")
    print("     CONGRATULATIONS!")
    print("          YOU WON!")
    print("==============================")
    print("The word was:", secret_word)

else:
    print(stages[6])
    print("\n==============================")
    print("          GAME OVER!")
    print("==============================")
    print("The correct word was:", secret_word)

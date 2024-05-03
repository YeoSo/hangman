from hangman_art import logo
import random
from hangman_words import word_list
import string

alphabet = list(string.ascii_lowercase)  # Generates a list of lowercase alphabets
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

try:
    with open("chosen_word.txt", "w") as file:
        file.write(chosen_word)
except Exception as e:
    print(f"An error occurred while writing the chosen word to file: {e}")

end_of_game = False
lives = 6

print(logo)

# Testing code
# print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

name = input("What's your name?: ")
print(f"Welcome {name.title()}. You have 6 lives to try. Good luck!\n")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess not in alphabet:
        print("Please enter a valid alphabet.")
        continue  # Skip the rest of the loop and start over

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True

    # Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages

    print(stages[lives])
    if lives == 1:
        print(f"You have {lives} life left.")
    elif lives == 0:
        print(f"You have no more life left.")
    else:
        print(f"You have {lives} lives left.")

# Check if user has got all letters.
if "_" not in display:
    print(f"You win! Well done {name}")
else:
    print("Game Over!")

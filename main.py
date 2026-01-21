# Using hangman_art and hangman_words to keep main code cleaner
import random
import hangman_art
import hangman_words
# Starter and placeholder vars
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
placeholder = ""
matched_letters = []
tracked_letters = []
game_over = False
lives = 6
print(f"{hangman_art.logo}\n")

# Prints out placeholder showing how many char the word is
for i in chosen_word:
    placeholder += "_"

print(f"Word to guess {placeholder}")
# Main while loop. This will end when game_over = True
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

# Continue is used so the loop does not complete
    if guess in tracked_letters:
        print(f"You guessed the letter {guess} already")
        continue
    tracked_letters.append(guess)

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            if letter not in matched_letters:
                matched_letters.append(letter)
        elif letter in matched_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if "_" not in display:
        print("****************************YOU WIN****************************")
        game_over = True
    elif lives == 0:
        print(f"***********************IT WAS {chosen_word} YOU LOSE**********************")
        game_over = True

    print(hangman_art.stages[lives])

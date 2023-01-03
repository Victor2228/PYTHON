import random

with open('hangman_words.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]

lives = 7
guesses = []
used = []
done = False
while not done:
    print(f"USED WORDS= {guesses}")
    print("")
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print("")
    print("")
    guess = input(f"Lives left= {lives}, Your Guess: ")
    print("")
    guesses.append(guess.lower())
    used.append(guess.lower())
    if guess.lower() not in word.lower():
        lives -= 1
        if lives == 0:
            break
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False
if done:
    print(f"CORRECT! THE WORD IS {word}. YOU WON!")
else:
    print(f"SORRY! THE WORD IS {word}. YOU LOST!")

import random
import time
import os
simon = "RGBY"
word = ""
print("__________GAME START__________")
for score in range(0, 10):
    word += random.choice(simon)
    for words in word:
        print(words)
        time.sleep(1.5)
        os.system("cls")
    guess = input("REPEAT: ")
    os.system("cls")
    if guess != word:
        break

print(f"GAME OVER! YOUR FINAL SCORE= {score}")


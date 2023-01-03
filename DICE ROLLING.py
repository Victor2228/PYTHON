import random
import time
print("______DICE ROLL______")


def roll():
    a = random.randint(1, 7)
    return a


str(input("ROLL THE DICE: Press ENTER "))
print("Dice rolling ", end="")
for i in 0, 20:
    time.sleep(0.5)
    print(".", end="")
time.sleep(0.5)
b = roll()
print(f"\n{b}")
while 1:
    c = str(input("WANT TO ROLL AGAIN? Y=Yes N=No  "))
    if c == 'Y' or c == 'y':
        str(input("ROLL THE DICE: Press ENTER "))
        print("Dice rolling ", end="")
        for i in (0, 4):
            time.sleep(0.5)
            print(".", end="")
        time.sleep(0.5)
        b = roll()
        print(f"\n{b}")
    else:
        break
    
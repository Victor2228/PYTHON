import random

a = random.randint(1, 101)
print("__________NUMBER GUESSING__________")
x = 4
z = 3
while x > 0:
    print("LIVES= " + str(x) + "\n")
    b = input("ENTER THE SUITABLE NUMBER= ")
    if a == b:
        print("RIGHT GUESS")
        break
    else:
        print("WRONG!!!TRY AGAIN\n")
        y = str(input("WANT A HINT?? Y=Yes N=No  "))
        if y == 'Y' or y == 'y':
            if z == 3:
                if a % 2 == 0:
                    print("IT IS AN EVEN NUMBER")
                else:
                    print("IT IS AN ODD NUMBER")
                z = z - 1
                print(str(z) + " HINTS ARE LEFT")
            elif z == 2:
                if a > 50:
                    print("IT IS GREATER THAN 50 AND LESS THAN 100")
                else:
                    print("IT IS LESS THAN 50 AND GREATER THAN 0")
                z = z - 1
                print(str(z) + " HINTS ARE LEFT")
            elif z == 1:
                if a < 10:
                    print("IT IS A SINGLE-DIGIT NUMBER")
                else:
                    print("IT IS A DOUBLE-DIGIT NUMBER")
                z = z - 1
                print(str(z) + " HINTS ARE LEFT")
            else:
                print("SORRY, " + str(z) + " HINTS ARE LEFT")
        x = x - 1
if x == 0:
    print("\nTHE NUMBER IS " + str(a))

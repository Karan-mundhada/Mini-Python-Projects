import random
import sys
while True:
    try:
        x = int(input("Level: "))
        if(0 < x < 100):
            ans = random.randint(1, x)
            while True:
                a = int(input("Guess: "))
                if(a == ans):
                    print("Just Right!")
                    sys.exit()
                elif(a < ans):
                    print("Too Small!")
                    pass
                else:
                    print("Too Big!")
                    pass
        else: 
            print("Input Valid Level")
    except ValueError:
        pass
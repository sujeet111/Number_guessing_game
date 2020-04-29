import random


def start_game(number):
    count=0
    while True:
        try:
            guess=int(input("pick a number between 1-10:  "))
            
        except ValueError:
            print("Plase enter an integer")
            continue
        if guess > 11 or guess < 0:
                print("Plase enter a number between 1-10")
                continue
        count+=1
        if guess > number:
            print ("It's lower")
        elif guess < number:
            print("It's higher")
        elif guess == number:
            print("You got it! it took you {} tries.\n".format(count))
            return count
        
            
    


# Kick off the program by calling the start_game function.
score=0
hi_score=[]
print("""
    -----------------------------------------------
      ***welcome  to the Number guessing game***
    -----------------------------------------------
    """)

while True:
    solution = random.randint(1,10)
    score = start_game(solution)
    hi_score.append(score)
    hi_score.sort()
    loop = input("Would you like to play again?  [y]es/[n]o:  ")
    if loop == "y":
        print("\n\n\nThe high score is {}".format(hi_score[0]))
        continue
    elif loop == "n":
        break
    else:
        print("invalid input")
        break
     
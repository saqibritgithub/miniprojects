import random
animal=["horse","goat","cat","dog"]
computer_guess=random.choice(animal)
char=["loyalty","healthy milk","lions grandmother","bark loudlly"]
user_choice=random.choice(char)
if (computer_guess=="horse" and user_choice=="loyalty"):
    print("computer_guess is :", computer_guess)
    print("user guess is :",user_choice)
    print("well guessed")
elif (computer_guess=="goat" and user_choice=="healthy milk"):
    print("computer_guess is :", computer_guess)
    print("user guess is :", user_choice)
    print("well guessed")
elif (computer_guess=="cat" and user_choice=="lions grandmother"):
    print("computer_guess is :", computer_guess)
    print("user guess is :", user_choice)
    print("well guessed")
elif (computer_guess=="dog" and user_choice=="bark loudlly"):
    print("computer_guess is :", computer_guess)
    print("user guess is :", user_choice)
    print("well guessed")
else:
    print("invalid operatin")
answer = int(input("Welcome to Atharva's Health Spot!\n What would you like me to help you wtih?\nPress 1: If you are bored and want to play a game. \nPress 2: If you just want to interact and enjo[...]
if answer == 1:
    response1 = int(input(("Wow, so you want to play a game huh?\nPress 1 to play (Guess the number)\nPress 2 to play (Rock,Paper,Scissors)\nYour response: ")))
    if response1 == 1:

        import random

        top_of_range = int(input("Type a number: "))

        if top_of_range.is_integer():
            top_of_range = int(top_of_range)

            if top_of_range <= 0:
                print("Please type a number larger than 0 next time")
                quit()
        else:
            print("Please type a number next time!")
            quit()

        random_number = random.randint(0, top_of_range)

        while True:
            user_guess = input("Make a guess: ")
            if user_guess.isdigit():
                user_guess = int(user_guess)
            else:
                print("Please type a number next time!")
                continue
            if user_guess == random_number:
                print("You got it right")
                break
            else:
                print("You got it wrong!")



    elif response1 == 2:
        print("Alright, Rock Paper Scissors it is!")

        import random

        user_wins = 0
        computer_wins = 0

        options = ["rock", "paper", "scissors"]

        # FIXED: Moved game logic inside the loop so it repeats correctly
        while True:
            user_input = input("Type Rock Paper Scissors or Q to quit: ")
            if user_input == "Q":
                break

            if user_input.lower() not in ["rock", "paper", "scissors"]:
                print("Invalid choice! Please enter rock, paper, or scissors.")
                continue

            random_number = random.randint(0, 2)

            computer_pick = options[random_number]

            print("Computer picked", computer_pick + ".")

            if user_input == "rock" and computer_pick == "scissors":
                print("You won")
                user_wins += 1
            elif user_input == "paper" and computer_pick == "rock":
                print("You won")
                user_wins += 1
            elif user_input == "scissors" and computer_pick == "paper":
                print("You won")
                user_wins += 1
            elif user_input == computer_pick:
                print("It's a tie!")
            else:
                print("You lost!")
                computer_wins += 1

        print("You won", user_wins, "times.")
        print("The computer won", computer_wins, "times.")
        print("GoodBye!")
else:
    print("So you want to interact with me?\n Alright! \n How are you doing?")

    import time
    response2 = int(input("Press 1 if you are happy! \n Press 2 if you are sad!\nYour response: "))
    if response2 == 1:
        print("Well have a good day then! Just have a good sleep and play this quiz sometime later again!")
    if response2  == 2:
        print("Why you sad? Let us cheer you up by walking a few steps.\n Come on! You can do this!")
        time.sleep(2)
        user_input = None
        user_input = int(input("Write down how much you have walked: "))
        while True:
            print("You can do this! Keep Walking! Hope you felt fit after this exercise!")
            break

# FIXED: Get actual rating input instead of hardcoded list comparison
rating = int(input("Rate your experience (1-5): "))
if rating in [1, 2, 3]:
    print("Let us know how we can do better!")
elif rating in [4, 5]:
    print("Thank you for your feedback!")
else:
    print("Thank you for giving me spending time on me!\n See you next time!\n Bye and Have a good day!")

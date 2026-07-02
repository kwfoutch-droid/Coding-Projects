import random

choices = ["rock", "paper", "scissors"]
score = 0

def play_rock_paper_scissors():
    global score
    cpu_choice = random.choice(choices)
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return

    print(f"CPU chose: {cpu_choice}")

    if user_choice == cpu_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and cpu_choice == "scissors"):
        print("You win! Congratulations.")
        score += 1
    elif (user_choice == "paper" and cpu_choice == "rock"):
        print("You win! Congratulations.")
        score += 1
    elif user_choice == "scissors" and cpu_choice == "paper":
        print("You win! Congratulations.")
        score += 1
    elif user_choice == "scissors" and cpu_choice == "rock":
        print("You lose! CPU wins.")
    elif user_choice == "paper" and cpu_choice == "scissors":
        print("You lose! CPU wins.")
    elif user_choice == "rock" and cpu_choice == "paper":
        print("You lose! CPU wins.")


playing = True
while playing:
    play_rock_paper_scissors()
    print(f"Your score: {score}")
    again = input("Play again? (y/n): ").lower()

    if again != "y":
        playing = False
    
print("Thanks for playing!")
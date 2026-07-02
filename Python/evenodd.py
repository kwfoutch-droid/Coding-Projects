number = int(input("Enter a number: "))
playing = False


def even_or_odd(number):
    playing = True
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

while not playing:
    even_or_odd(number)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        number = int(input("Enter a number: "))
    else:
        playing = True
        print("Thanks for playing!")
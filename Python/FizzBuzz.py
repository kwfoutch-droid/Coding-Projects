

playing = False


number = int(input("Enter a number: "))



def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print(f"The number {number} is FizzBuzz.")
    elif number % 3 == 0:
        print(f"The number {number} is Fizz.")
    elif number % 5 == 0:
        print(f"The number {number} is Buzz.")
    else:
        print(f"The number {number} is neither Fizz nor Buzz.")

while not playing:
    fizz_buzz(number)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        number = int(input("Enter a number: "))
    else:
        playing = True
        print("Thanks for playing!")
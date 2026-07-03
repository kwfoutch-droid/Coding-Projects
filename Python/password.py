
import random



going = False




while going == False:
    password_range = int(input("How many characters do you wish to have in your password: "))
    finished = False
    password = ''
    going = True
    characters = "abcdefghijklmnopqrstuvwxyz!_1234567890"

    for i in range(password_range):
        if i ==0:
            password += random.choice(characters.upper())
            
        else:
            password += random.choice(characters)
            
    finished = True

    if (len(password)) != password_range and finished:
        change = (len(password)) - password_range
        if change < 0:
            change = abs(change)
            for x in range(change):
                password += random.choice(characters)
        else:
            password = password[: -change]
    going = False


    print(password)
    print(len(password))
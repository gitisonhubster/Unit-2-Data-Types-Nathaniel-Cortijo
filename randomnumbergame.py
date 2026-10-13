import random

random_number = random.randint(1,256)
user_history = []
while not random_number in user_history:
    number_input = float(input("guess a number"))
    user_history.append(number_input)
    print(user_history)
    if number_input == random_number:
        print("You Won :D :D :D !!!!!!!!!!!! (YIPEEEEEEEEEEEE!!!!!!!!!) !!!!!! (YAYYYYYYYYYYYY!!!!!!!!!!!) !!!!!!!!!!!")
        break
    else:
        print("WRONG D:<")
        if number_input < random_number:
            print("GO HIGHER!!!!!!!")
        if number_input > random_number:
           print("GO LOWER!!!!!!!") 


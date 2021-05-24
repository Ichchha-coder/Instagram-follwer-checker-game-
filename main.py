score = 0
end_of_game = False
start_of_second = False

import random

from game import data

from art import logo
from art import vs

print(logo)

while not end_of_game:
    if start_of_second == False:
        first_choice = random.choice(data)
        # print(first_choice)
        print("Your first choice is:")
        print(first_choice["name"])
        follower_1 = first_choice["follower_count"]

    print(vs)

    second_choice = random.choice(data)
    # print(second_choice)
    print("Your second_choice is :")
    print(second_choice["name"])
    follower_2 = second_choice["follower_count"]

    choice = input(("Choose the one with larger follower A or B :"))
    if choice == "A" and follower_1 > follower_2 or choice == "B" and follower_2 > follower_1:
        score += 1
        print(f"The score is {score}")

        start_of_second = True
        if start_of_second == True:
            first_choice = second_choice
            print("Your first choice is :")
            # print(first_choice)
            print(first_choice["name"])
            follower_1 = first_choice["follower_count"]




    elif follower_1 == follower_2:
        second_choice = random.choice(data)
        print(second_choice)
        print("scond_choice[name]")
        follower_2 = second_choice["follower_count"]

    else:
        print("The game has ended")
        print(f"Your final score is {score}")
        end_of_game = True

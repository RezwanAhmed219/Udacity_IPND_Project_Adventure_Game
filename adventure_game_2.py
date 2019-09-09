import random
import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("Months of planning have brough you all here.")
    print_pause("People from all over the world have gathered here today.")
    print_pause("'It is now or never' you think.'")
    print_pause("Thousands of curious minds standing infront of the Area 51 \n"
                "gate, probably thinks the same.")
    print_pause("But you fear the unknown. Do you want to go inside(1) or \n"
                "turn back(2) at the last minute?")


def takedecision():
    path = ""
    while path != "1" and path != "2":
        path = input("Which decision will you take?   (1 or 2): ")


def checkPath(decision):
    print_pause("The gates open")
    print_pause("Even in their wildest imaginations, no one expected it to \n"
                "actually happen")

    correctPath = random.randint(1, 2)

    if decision == str(correctPath):
        print_pause("The government had set a trap, inside was a large open \n"
                    "field labelled as 'Nuclear testing zone'.")
        print_pause("You look above and you see two planes dropping bombs.")
        print_pause("It was a set up. The government wanted to get rid of \n"
                    "the people who asked too many questions.")
        print_pause("GAME OVER")
    else:
        print_pause("A futuristic city lie ahead.")
        print_pause("A lot of different creatures and aliens were working \n"
                    "side by side by Humans.")
        print_pause("Was this the future of Humanity being planned inside \n"
                    "Area 51?")
        print_pause("Tune in to find out in the next episode.")
        print_pause("GAME OVER")


def ending():
    print_pause("Would you like to play again? (y/n)")
    answer = input("1. y\n"
                   "2. n\n")
    if answer == 'y':
        print_pause("Excellent!Restarting the game again")
        time.sleep(1)
        play_game()
    elif answer == 'n':
        print_pause("Thanks for playing, see you next time!")
    else:
        print_pause("Sorry, I don't understand.")
        ending()


def play_game():
    intro()
    choice = takedecision()
    checkPath(choice)
    ending()


if __name__ == '__main__':
    play_game()

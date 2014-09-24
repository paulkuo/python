# Rock-paper-scissors-lizard-Spock
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
names = [
    "rock",
    "Spock",
    "paper",
    "lizard",
    "scissors"
]

# helper functions

def name_to_number(name):
    for i in range(len(names)):
        if names[i] == name:
            return i
    return None

def number_to_name(number):
    if number >= 0 and number < len(names):
        return names[number]
    else:
        return None

def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    if player_number == None:
        print "Unknown choice"
    else:
        # print out the message for the player's choice
        print "Player chooses " + player_choice
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(len(names))

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice

    # compute difference of comp_number and player_number modulo five
    result = (player_number - comp_number) % len(names)

    # determine winner, print winner message
    if result == 0:
        print "Player and computer tie!"
    elif result <= 2:
        print "Player wins!"
    else:
        print "Computer wins!"

if __name__ == "__main__":
    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")

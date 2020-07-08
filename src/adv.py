from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#create a input parser that accepts direction commands
#parser should print error if wrong choice is inputed
wrongpath = "There is no path in that direction"

player = Player("Ch1efW1z", room['outside'])

while True:
    print(player.startingroom)
    playerinput = input("Choose a direction to travel north, south, east, west or q to quit: ")
    try:
        if(playerinput == 'q'):
            break
        elif(playerinput != 'north' and playerinput != 'south' and playerinput != 'east' and playerinput != 'west'):
            print("You must select a direction or q to quit")
            print(playerinput)
        elif(playerinput == 'north'):
            if(player.startingroom.n_to == 'none'):
                print(wrongpath)
            else:
                player.startingroom = player.startingroom.n_to
        elif(playerinput == 'south'):
            if(player.startingroom.s_to == 'none'):
                print(wrongpath)
            else:
                player.startingroom = player.startingroom.s_to
        elif(playerinput == 'east'):
            if(player.startingroom.e_to == 'none'):
                print(wrongpath)
            else:
                player.startingroom = player.startingroom.e_to
        elif(playerinput == 'west'):
            if(player.startingroom.w_to == 'none'):
                print(wrongpath)
            else:
                player.startingroom = player.startingroom.w_to
    except ValueError:
        print("Please enter a valid command")
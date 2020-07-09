from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "The cave mount to the north is a dark hole calling for you to enter"),

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

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'



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
player = Player('You', 'outside')

userChoice = ['north', 'south', 'east', 'west', 'quit']
choice = 0

Rustysword = Item('Rusty sword', 'This sword may help you survive the perils that lie ahead')
room['foyer'].add_item(Rustysword)

print(f'\n  You are standing before an  {room[player.location].name}  {room[player.location].description}')

while choice != 'quit':
    choice = input('\nChoose a direction: ')
    try:
        if choice == 'north':
            player.location = room[player.location].n_to
            print(f'\n  You walk through the dark mouth of the cave into a strange {room[player.location].name} \n\n  {room[player.location].description}')
            if len(room[player.location].items) != 0:
                print(f'\n  You see a {room[player.location].items[0]}')

        if choice == 'south':
            player.location = room[player.location].s_to
            print(f'\n  You walk south into the {room[player.location].name} \n\n  {room[player.location].description}')
            if len(room[player.location].items) != 0:
                print(f'\n  You see a {room[player.location].items[0]}')

        if choice == 'east':
            player.location = room[player.location].e_to
            print(f'\n  You walk east into the {room[player.location].name} \n\n   {room[player.location].description}')
            if len(room[player.location].items) != 0:
                print(f'\n  You see a {room[player.location].items[0]}')

        if choice == 'west':
            player.location = room[player.location].w_to
            print(f'\n  You walk west into the {room[player.location].name} \n\n   {room[player.location].description}')
            if len(room[player.location].items) != 0:
                print(f'\n  You see a {room[player.location].items[0]}')

        if choice not in userChoice:
            print('\n   That is not a direction.  Type c to see the controls')

    except:
        print("\n   You can't go that way")
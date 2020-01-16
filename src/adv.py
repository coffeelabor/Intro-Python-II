from room import Room
from player import Player
# Declare all the rooms

player = {
    "readyPlayerOne": Player("Reed", "outside")
}

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

# playerRoom = ['outside']

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

#Create a player
#let player input their name

player = Player(input("Player name: "), room["outside"])
print(player.current_room)

directions = ["n", "s", "e", "w",]

print(player.name)

print(room['outside'].n_to)



#Create basic REPL loop 
while True:
    #Read command
    cmd = input("~~> ".lower())
    #check if its n/s/e/w/q
    if cmd in directions:
        #make palyer travel in that direaction
        player.travel(cmd)
    elif cmd == "q":
        print("Later")
        break
    else:
        print('dont be lame, just type one of the commands')
    #if so ececute the proper command


'''

Day 2 MVP

Make rooms able to hold multiple items
    I think I need to make a new file with a new class for items
    maybe I can just copy the way the rooms interact with the player

Make the player able to carry multiple items
    If I just swicth a player being in a room with a item being with a player

Add items to the game that the user can carry around
    This is where I think i need to add a new file with a class

Add `get [ITEM_NAME]` and `drop [ITEM_NAME]` commands to the parser
    this is where I can copy the rooms/player and have items 'leave' and 'enter' a player

'''
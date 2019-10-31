from room import Room
from player import Player
# Declare all the rooms

player = {
    "playerOne": Player("Reed", 'outside')
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

# Make a new player object that is currently in the 'outside' room.

playerRoom = room['outside']

stop = False

while not stop:
    print(f'You see a {playerRoom.name}, {playerRoom.option}')
    print("############## Your Move! #####################")
    move = input('What way do you want to go: ')

    if move.lower() == 'n':
        playerRoom = playerRoom.n_to
    elif move.lower() == 's':
        playerRoom = playerRoom.s_to
    elif move.lower() == 'e':
        playerRoom = playerRoom.e_to
    elif move.lower() == 'w':
        playerRoom = playerRoom.w_to
    elif move.lower() == 'q':
        stop = True
    else:
        print("you cant do that")
    print(f"######### Your in the {playerRoom.name} ##############")
print("############Player##############")
user = player['playerOne'].name
print(user)

print("############Room##############")
currentRoom = room['outside'].n_to.name
print(currentRoom)

print("############Room Loop##############")
for k, v in room.items():
    print(k, v.name, v.option)

# print("############Move##############")
# move = input('What way do you want to go: ')
# moveDir(move)


# print(room)

# while True:
#     currentRoom = Room.name[1]
#     print(currentRoom)

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

############# Junk Code ######################
# def moveDir(move):
#     if (move == 'n'):
#         print('north')
#     elif (move == 's'):
#         print('south')
#     elif (move == 'e'):
#         print('east')
#     elif (move == 'w'):
#         print('west')
#     else:
#         print('wrong')

# directions = {
#     'n': 'n_to',
#     's': 's_to',
#     'w': 'w_to',
#     'e': 'e_to'
# }

# class Player:
#     def __init__(self, name):
#         self.name = name
# Write a loop that:

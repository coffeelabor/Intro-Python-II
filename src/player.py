# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    #init player with name
    def __init__(self, name, starting_room):
        self.name = name  
        # Player also has attr current_room
        self.current_room = starting_room

    def travel(self, direction):
        # Player should be able to move
        # print(f"Player should travel {direction}")
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("Cant go there, its a wall")
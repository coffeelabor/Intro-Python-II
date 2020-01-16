# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    #init player with name
    #
    def __init__(self, name, location, starting_room):
        self.name = None
        self.location = location   
        # Player also has attr current_room
    def travel(self, direction):
        pass
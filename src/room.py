# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, option):
        self.name = name
        self.option = option

        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

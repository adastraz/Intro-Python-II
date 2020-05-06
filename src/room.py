# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, items, description, n_to, s_to, e_to, w_to):
        self.name = name
        self.items = items
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    def __str__(self):
        return f'You are in the room : {self.name} \nThere are these items from within : {self.items} \nDescription : {self.description}'
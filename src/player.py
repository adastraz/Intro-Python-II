# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'{self.name}'

    def add_to_inv(self, item):
        if len(self.inventory) < 3:
            self.inventory.append(item)
        else:
            print('You have too many items!\n')

    def drop_item(self, index):
        if len(self.inventory) > 0:
            self.inventory.remove(self.inventory[index-1])
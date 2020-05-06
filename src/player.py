# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def __str__(self):
        return f'Characters name : {self.name}'

while True: 
    username = input('Please choose your characters name : ')
    if len(username) < 20:
        new_player = Player(username, 'one')
    else:
        print('your name is too long, under 20 characters')
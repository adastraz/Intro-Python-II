from room import Room
from player import Player
import os
clear = lambda: os.system('clear')

# Declare all the rooms
#nsew
room = {
    'outside': Room("Outside Cave Entrance", ['lantern', 'torch', 'flashlight'],"it's foggy, you see light coming from the north-west",None,None,None,None),
    'porch': Room("Porch", ['stick', 'club', 'batteries'],'You see a window to the north, but you cannot see through. Maybe there is a door nearby',None,None,None,None),
    'inside': Room('Inside', ['glass', 'wine'], 'You smashed open the window! Hopefully noone heard you...',None,None,None,None),
    'overlook': Room("Grand Overlook", ['daisy'], 'What a pretty daisy, if only it were daytime to see the view',None,None,None,None),
    'doorstep': Room('The Doorstep', ['flowerpot'],'The door is locked',None,None,None,None)
    # 'narrow': Room("Narrow Passage", []),
    # 'treasure': Room("Treasure Chamber", []),
    # 'ship': Room('Flying Dunchman', ['rum', 'gun', 'kraken heart']),
    # 'carnival': Room(),
    # 'cave':Room(),
    # 'basement':Room(),
    # 'bedroom': Room()
}


# Link rooms together
room['outside'].n_to = room['porch']
room['porch'].s_to = room['outside']
room['porch'].w_to = room['doorstep']
room['porch'].e_to = room['overlook']
room['doorstep'].e_to = room['porch']
room['overlook'].w_to = room['porch']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#
start_game = False
username = input('Please choose your characters name : ')
if len(username) < 20:
    new_player = Player(username, room['outside'])
    start_game = True
else:   
    print('your name is too long, under 20 characters')

while start_game == True:
    print(f'Welcome to the Adventure Game : {new_player.name}\n')
    print(f'{new_player.current_room}\n')
    action_selection = input('Pick up item (1), Travel to another room (2), Drop items (3), Help (h): ')
    if action_selection == 'q':
        break
    elif action_selection == 'h':
        clear()
        print('Travel : w = North, a = West, s = South, d = East \nList items: i\nHelp: h')
    elif action_selection == 'i':
        clear()
        if len(new_player.inventory) > 0:
            print(f'Inventory : {new_player.inventory}')
        else:
            print("You haven't picked up any items")

    try:
        select = int(action_selection)
        if select == 2: 
            room_loop = True
            while room_loop == True:
                room_selection = input('\nWhere would you like to go? (room description will help!) \n W(n)A(w)S(s)D(e) for North, West, South, or East or (Q)uit: ')
                if room_selection == 'w' and new_player.current_room.n_to != None:
                    new_player.current_room = new_player.current_room.n_to
                    room_loop = False
                    clear()
                elif room_selection == 'a' and new_player.current_room.w_to != None:
                    new_player.current_room = new_player.current_room.w_to
                    room_loop = False
                    clear()
                elif room_selection == 's' and new_player.current_room.s_to != None:
                    new_player.current_room = new_player.current_room.s_to
                    room_loop = False
                    clear()
                elif room_selection == 'd' and new_player.current_room.e_to != None:
                    new_player.current_room = new_player.current_room.e_to
                    room_loop = False
                    clear()
                elif room_selection == 'q' :
                    room_loop = False
                    start_game = False
                    break
                elif room_selection == 'x':
                    clear()
                    break
                else: 
                    print('Please select a valid room! Read the room description for details \n')

        if select == 1:
            item_loop = True
            while item_loop == True:
                item_selection = input(f'Select item to pickup but number (1,2,3,etc) {new_player.current_room.items} : ')
                if item_selection == 'x':
                    clear()
                    break
                item_select = int(item_selection)
                try:
                    if new_player.current_room.items[item_select-1]:
                        new_player.add_to_inv(new_player.current_room.items[item_select-1])
                        if new_player.current_room.items[item_select-1] == 'club':
                            room['porch'].n_to = room['inside']
                            room['inside'].s_to = room['porch']
                        new_player.current_room.remove_items(item_select)
                        
                        clear()
                        print(f'\nYour inventory : {new_player.inventory}')
                        item_loop = False
                except IndexError:
                    print('Please select a valid item from within the list\n')

        if select == 3 and len(new_player.inventory) > 0:
            drop_loop = True
            while drop_loop == True:
                drop_selection = input(f'Drop item from inventory {new_player.inventory}')
                drop_select = int(drop_selection)
                try:
                    if new_player.inventory[drop_select-1] and len(new_player.inventory) > 0:
                        new_player.current_room.dropped_item(new_player.inventory[drop_select-1])
                        new_player.drop_item(drop_select)
                        clear()
                        print(f'\nYour inventory : {new_player.inventory}\n')
                        drop_loop = False
                except IndexError:
                    print("You don't have that many items")
        if select == 3 and len(new_player.inventory) == 0:
            clear()
            print('\nYou do not have any items\n')
        if ['daisy', 'flowerpot'] == new_player.current_room.items and ['wine'] == new_player.inventory:
            clear()
            input('\n********\n\nYOU WIN!!!\n\n*********\n\npress any button to exit')
            break
    except ValueError: 
        clear()
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

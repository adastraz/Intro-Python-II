from room import Room

# Declare all the rooms
#nsew
room = {
    'outside': Room("Outside Cave Entrance", ['lantern', 'torch', 'flashlight'],"it's foggy, you see light coming from the north-west",'one',None,None,'four'),
    'foyer': Room("Foyer", ['lantern', 'torch', 'flashlight'],'description','one',None,None,'four'),
    # 'overlook': Room("Grand Overlook", []),
    # 'narrow': Room("Narrow Passage", []),
    # 'treasure': Room("Treasure Chamber", []),
    # 'ship': Room('Flying Dunchman', ['rum', 'gun', 'kraken heart']),
    # 'carnival': Room(),
    # 'cave':Room(),
    # 'basement':Room(),
    # 'bedroom': Room()
}


# Link rooms together
room['outside'].n_to = room['foyer']
print(room['outside'])
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

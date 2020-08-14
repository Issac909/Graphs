from room import Room
from player import Player
from world import World

import os

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
dirpath = os.path.dirname(os.path.abspath(__file__))
# map_file = dirpath + "/maps/main_maze.txt"
# map_file = dirpath + "maps/test_cross.txt"
# map_file = dirpath + "maps/test_loop.txt"
# map_file = dirpath + "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
traversal_path = []
# Rooms visited
visited =  {}
# Used to store the opposite direction for back travel
direction = {"n" : "s", "e": "w", "s":"n", "w": "e" } 
# Store the directions
reverse_path = [] 
# marking the id of room as exit
visited[0] = player.current_room.get_exits()
# while rooms visited is less than the total number of rooms
while len(visited) < len(room_graph) - 1:
    # if room is not visited yet
    if player.current_room.id not in visited: 
        # mark the exits from the current room
        visited[player.current_room.id] = player.current_room.get_exits()
        # store the previous room traveled
        prev = reverse_path[-1]
        # remove last exit from exits dictionary
        visited[player.current_room.id].remove(prev)
        
    # when no rooms to explore
    while len(visited[player.current_room.id]) < 1: 
        # store the last direction
        reverse = reverse_path.pop()
        # add the reverse direction to traversal path
        traversal_path.append(reverse)
        # move player to previous location
        player.travel(reverse)
    
    # store the first exit in []
    exit_way = visited[player.current_room.id].pop(0)
    # add exit to traversal path
    traversal_path.append(exit_way) 
    # add to reverse path using direction entered from 
    reverse_path.append(direction[exit_way])
    # move player to first exit in []
    player.travel(exit_way)

# 1004 moves, 500 rooms

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

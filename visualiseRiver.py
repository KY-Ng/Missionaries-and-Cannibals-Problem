#! python 3
# -*- coding: utf-8 -*-
"""
Missionaries and Cannibals Problem
"""

import crossRiver as cr

numMissionaries = 3
numCannibals = numMissionaries
numBoat = 1

river = cr.Graph(numMissionaries, numCannibals, numBoat)
river.generate_graph()
path = river.find_path((numMissionaries, numCannibals, numBoat), (0,0,0))
#print(path)

# Drawing parts
missionaries = "(M)"
cannibals = "[C]"
leftBoat = "|<__>__"
rightWater = "________|"
rightBoat = "__<__>|"
leftWater = "|________"

def drawState(state):
    '''
    state[0]: numMissionaries
    state[1]: numCannibals
    state[2]: numBoat
    '''
    leftMargin = len(missionaries)*numMissionaries + len(cannibals)*numCannibals
    print((missionaries*state[0]+cannibals*state[1]).rjust(leftMargin), end="")
    if state[2] == 1:
        print(leftBoat+rightWater, end="")
    elif state[2] == 0:
        print(leftWater+rightBoat, end="")
    print(missionaries*(numMissionaries-state[0])+cannibals*(numCannibals-state[1]))

# Start Visualisation
print()
print("Start".rjust(28))
for state in path:
    drawState(state)
print("End".rjust(27))

#print(missionaries, cannibals, boat+water)
#drawState((3,3,1))
#drawState((0,0,0))



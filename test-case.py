#! python 3
# -*- coding: utf-8 -*-
"""
Missionaries and Cannibals Problem
"""

import crossRiver as cr
import pprint

numMissionaries = 3
numCannibals = numMissionaries
numBoat = 1

def testFunction(func):
    river = cr.Graph(numMissionaries, numCannibals, numBoat)
    print("Testing Graph.{}() ...".format(func))
    # check_valid_state
    if func == 'check_valid_state':
        case1 = river.check_valid_state((3,3,1)) == True
        case2 = river.check_valid_state((2,2,1)) == True
        case3 = river.check_valid_state((2,3,1)) == False
        case4 = river.check_valid_state((0,0,0)) == True
        case5 = river.check_valid_state((-1,3,1)) == False
        case6 = river.check_valid_state((2,-1,1)) == False
        if case1 and case2 and case3 and case4 and case5 and case6:
            print("Done checking! No problem")
        
    # find_next_vertex
    elif func == 'find_next_vertex':
        testPoint = [(3,3,1), (2,2,0)]
        for point in testPoint:
            river.find_next_vertex(point)
    
        for edge in river.graph()[(3,3,1)]:
            if edge not in [(3,2,0), (3,1,0), (2,2,0)]:
                print("{} is not included as a edge of {}".format(edge, (3,3,1)))
                case1 = False
            else:
                case1 = True
                
        for edge in river.graph()[(2,2,0)]:
            if edge not in [(3,3,1), (3,2,1)]:
                print("{} is not included as a edge of {}".format(edge, (2,2,0)))
                case2 = False
            else:
                case2 = True
                
        if case1 and case2 == True:
            print("Done checking! No problem")
            
    # generate_graph
    elif func == 'generate_graph':
        river.generate_graph()
        pprint.pprint(river.graph())
#        print('\n', river.graph())
#        print(len(river.graph()) == 16) # should have 16 states when numMissionaries = 3
        
    elif func == 'find_path':
        river.generate_graph()
        print("\nFinding path...")
        path = river.find_path((numMissionaries, numCannibals, numBoat), (0,0,0))
        pprint.pprint(path)
        
    elif func == 'find_all_path':
        river.generate_graph()
        print("\nFinding path...")
        paths = river.find_all_path((numMissionaries, numCannibals, numBoat), (0,0,0))
        for n in range(len(paths)):
            print("Path {}: {}\nDistance: {}\n".format(n+1, paths[n], len(paths[n])))

#testFunction('check_valid_state')    
#testFunction('find_next_vertex')
#testFunction('generate_graph')
testFunction('find_path')
#testFunction('find_all_path')

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:09:01 2019

@author: Asus

Missionaries and Cannibals Problem
"""

# Variables
'''
number of missionaries, number of cannibals, number of boat
number of missionaries = number of cannibals
number of boat = 1
'''
numMissionaries = 3
numCannibals = 3
numBoat = 1

# Graph Object
class Graph(object):
    def __init__(self, numMissionaries, numCannibals, numBoat):
        '''
        store graph and variables
        representation of state: (m, c, b) # (numMissionaries, numCannibals, numBoat)
        only show the representation of left-side of the river (starting side)
        ''' 
        self.numMissionaries = numMissionaries
        self.numCannibals = numCannibals
        self.numBoat = numBoat
        self.startVertex = (self.numMissionaries, self.numCannibals, self.numBoat)
        self.endVertex = (0, 0, 0)
        
        self.graph = {
                self.startVertex: []
                }
    
    def vertices(self):
        '''return vertices of the graph'''
        return self.graph.keys()
       
    def edges(self):
        '''return edges of the graph'''
        return self.graph.values()
       
    def add_vertex(self, vertex):
        '''add vertex into graph if vertex does not exist in grpah'''
       
    def add_edge(self, fromVertex, toVertex):
        '''add egde from fromVertex to toVertex'''
       
    def check_valid_state(self, vertex):
        '''
        vertex: tuple
        check the validity of the vertex provided based on rules provided
        rules:
            when m = 0 or m = numMissionaries, 0 <= c <= numCannibals
            when 1 <= m <= numMissionaries-1, c = m
        return True if valid, else False
        '''
        if vertex[0] != 0 and vertex[0] != self.numMissionaries:
            if vertex[0] != vertex[1]:
                return False
            else: # c=m, continue basic test
                return vertex[0] <= self.numMissionaries and vertex[1] <= self.numCannibals
        else:
            return vertex[0] <= self.numMissionaries and vertex[1] <= self.numCannibals
       
    def find_next_vertex(self, currentVertex):
        '''
        add vertices (possible) to currentVertex
        possible: when check_valid_state() gives True
        '''

    def generate_graph(self):
        '''
        walk through every vectices exist in graph and generate their connected vertices respectively
        '''
        
    def find_path(self, startVertex, endVertex, path=None):
        '''find the path from startVertex to endVertex'''
       
def testFunction():
    river = Graph(numMissionaries, numCannibals, numBoat)
    
    # check_valid_state
    print("Testing Graph.check_valid_state() ...")
    case1 = river.check_valid_state((3,3,1)) == True
    case2 = river.check_valid_state((2,2,1)) == True
    case3 = river.check_valid_state((2,3,1)) == False
    case4 = river.check_valid_state((0,0,0)) == True
    if case1 and case2 and case3 and case4:
        print("Done checking! No problem")

testFunction()
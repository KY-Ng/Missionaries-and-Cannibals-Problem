#! python 3
# -*- coding: utf-8 -*-
"""
Missionaries and Cannibals Problem
"""

import pprint

# Variables
'''
number of missionaries, number of cannibals, number of boat
number of missionaries = number of cannibals
number of boat = 1 # able to carry 2 people
'''

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
        
        self.graph_dict = {
                self.startVertex: []
                }
    
    def vertices(self):
        '''return vertices of the graph'''
        return self.graph_dict.keys()
       
    def edges(self):
        '''return edges of the graph'''
        return self.graph_dict.values()
    
    def graph(self):
        '''return graph_dict'''
        return self.graph_dict
    
    def add_vertex(self, vertex):
        '''add vertex into graph if vertex does not exist in grpah'''
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
        
    def add_edge(self, fromVertex, toVertex):
        '''add egde from fromVertex to toVertex'''
        if fromVertex in self.graph_dict:
            if toVertex not in self.graph_dict[fromVertex]:
                self.graph_dict[fromVertex].append(toVertex)
        else:
           self.graph_dict[fromVertex] = [toVertex]
           
    def check_valid_state(self, vertex):
        '''
        vertex: tuple
        check the validity of the vertex provided based on rules provided
        rules:
            when m = 0 or m = numMissionaries, 0 <= c <= numCannibals
            when 1 <= m <= numMissionaries-1, c = m
        return True if valid, else False
        '''
        if vertex[0] < 0 or vertex[1] < 0: # numMissionaries and numCannibals >= 0 
            return False
        elif vertex[0] != 0 and vertex[0] != self.numMissionaries:
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
        # if currentVertex is not in self.graph_dict, append it
        self.add_vertex(currentVertex)
        
        vertexCandidates = [] # state(s) before validity check
        
        # Generate candidates for next vertex
        if currentVertex[2] == 1:
            for i in range(1, 3):
                vertexCandidates.append((currentVertex[0]-i, currentVertex[1], currentVertex[2]-1)) # (m-1, c, 0), (m-2, c, 0)
                vertexCandidates.append((currentVertex[0], currentVertex[1]-i, currentVertex[2]-1)) # (m, c-1, 0), (m, c-2, 0)
                if i == 1:
                    vertexCandidates.append((currentVertex[0]-i, currentVertex[1]-i, currentVertex[2]-1)) # (m-1, c-1, 0)
        elif currentVertex[2] == 0:
            for i in range(1, 3):
                vertexCandidates.append((currentVertex[0]+i, currentVertex[1], currentVertex[2]+1)) # (m+1, c, 1), (m+2, c, 1)
                vertexCandidates.append((currentVertex[0], currentVertex[1]+i, currentVertex[2]+1)) # (m, c+1, 1), (m, c+2, 1)
                if i == 1:
                    vertexCandidates.append((currentVertex[0]+i, currentVertex[1]+i, currentVertex[2]+1)) # (m+1, c+1, 1)
        else:
            print("{} is not a valid state".format(currentVertex))
            
        # Check validity of every state candidate and add them if valid
        for candidate_state in vertexCandidates:
            if self.check_valid_state(candidate_state) == True:
                self.add_edge(currentVertex, candidate_state)
        
    def generate_graph(self):
        '''
        walk through every vectices exist in graph and generate their connected vertices respectively
        '''
        lastRun = False
        count = 0
        while not lastRun:
            currentRun = list(self.vertices())[count:]
            if count != 0 and len(currentRun) == 0:
                lastRun = True
#            print("Current Run: {}".format(currentRun))
            for vertex in currentRun:
                print("Joining edges for {}".format(vertex))
                self.find_next_vertex(vertex)
                for connectedVertex in self.graph_dict[vertex]:
                    self.add_vertex(connectedVertex)
#            pprint.pprint(self.graph())
            count += 1
            print()
        if (0,0,0) not in self.graph_dict:
            print("No solution")
        
    def find_path(self, startVertex, endVertex, path=None):
        '''find the path from startVertex to endVertex'''
       
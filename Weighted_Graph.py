#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:36:37 2017

author: Randy R. Davila
course: MATH 2305 - Discrete Mathematical Structures

In this python script we define a simple and weighted graph class object. This
object should be used to write Prim's and Kruskal's algorithms.
"""
#EDITED TO ALLOW FOR:
#1)ADDITION OF EDGES TO DICT
#2)REMOVAL OF EDGES FROM DICT
#3)RETURN OF EDGES AND VERTICIES AS LISTS AS WELL AS SETS
#4)USE THE SETUP (a,b) INSTEAD OF (1,2)
#5)INSTANTIATE CLASS WITH OR WITHOUT A PRE-EXISTING FILE


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import re

class Weighted_Graph(object):
    
    def __init__(self, edge_list_file=None):
       """ Set the edge list directory address """
       if(edge_list_file is None):
           self.edge_dict= {}
           self.isFromTxt=False
       else:
           self.edge_list_file=edge_list_file
           self.isFromTxt=True
           self.edge_dict = self.create_edge_dict()
           
    def __str__(self):
        #Called when the object is used in a print statement
        return(str(self.edge_dict))
        
    def create_edge_dict(self):
        """ Reads in the edge list from the provided directory address and 
            creates a edge dictionary where the keys are the edges and values
            are the corresponding edge weights. In particular, to access the
            value of edge (a,b), simply type edge_dict[(a,b)]"""
        edge_dict = dict()                                 # dict()=empty dictionary
        edge_list = np.loadtxt(self.edge_list_file, str)   # numpy 2-d array
        for row in edge_list:
            edge_dict[(row[0], row[1])] = row[2]           # Assign keys and values
        return edge_dict
    
    
    def add_edge(self,edge,value):
        #Adds the given edge and weight
        self.edge_dict[edge]=value
        
        
    def remove_edge(self,edge):
        #Removes the specified edge
        del self.edge_dict[edge]
        
    
    def get_weight(self,edge):
        #Returns the weight of the specified edge
        try:
            return self.edge_dict[edge]
        except KeyError:
            return None
    
    def edge_set(self):
        """ Returns the set of edges """
        return set(self.edge_dict.keys())
    
    
    def edge_list(self):
        #Returns the list of edges
        return list(self.edge_set())
    
    
    def vertex_set(self):
        """ Returns the set of vertices """
        vertex_set = set()                                 # set()= the empty set
        for e in self.edge_set():
            for v in e:
                vertex_set.add(v)
        return vertex_set
    
    
    def vertex_list(self):
        #Returns the list of vertices
        return list(self.vertex_set())
    
    
    def create_edge_list_file(self):
        # creates a temporary file of the current Weighted Graph
        fir=[]
        sec=[]
        weight=[]
        s=""
        for i in self.edge_dict:
            edge= re.findall("[a-z]",str(i))
            fir.append(edge[0])
            sec.append(edge[1])
            weight.append(self.get_weight(i))
        for k in range(0,len(fir)):
            s+=fir[k]+" "+sec[k]+" "+weight[k]+"\n"
        file=open("edgefile","w")
        file.write(s)
        file.close()
        self.edge_list_file="edgefile"
        
    
    def draw_graph(self):
        """ This function is used to visualize your weighted graph. The functions
            used inside are from the networkx library. """
        if(self.isFromTxt==False):    #when the edge list was user generated 
            self.create_edge_list_file()
            
        G = nx.read_edgelist(self.edge_list_file, nodetype=str, data=(('weight',float),))
        e=[(u,v) for (u,v,d) in G.edges(data=True)]
        pos=nx.spring_layout(G) # positions for all nodes
        nx.draw_networkx_nodes(G,pos,node_size=250) # nodes
        nx.draw_networkx_edges(G,pos,edgelist=e,width=1) # edges
        
        # labels
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.axis('off')
        plt.show()
        
        
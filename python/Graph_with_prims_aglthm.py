#Graph implementation by Francisco Eduardo Balart Sanchez
# Prims minimum spanning tree algorithm python implementation 
# imports
import math
import random

data = ["v1","v2","v3","v4","v5","v6","v7"]
edges = [["v1","v2",2],["v1","v4",1],["v2","v4",3],["v2","v5",10],["v5","v7",6],["v7","v6",1],["v3","v1",4],["v3","v6",5],["v4","v3",2],["v4","v6",8],["v4","v7",4],["v4","v5",2]]

class Graph:
    """
    Simple Graph Class.
    """
    def __init__(self, data, edges):
        self._vertexes = []
        self._edges = []
        for vertex in data:
            self.insertVertex(vertex)
        for edge in edges:
            self.createEdges(edge)            
            
    def __str__(self):
        """
        Return human readable state
        """
        return "Class Graph: 		"+"\n" \
              +"Vertexes:	"+str(self._vertexes)+"\n" \
              +"Edges: 				"+str(self._edges)+"\n"
    
    def insertVertex(self, vertex):
        vertexobj = Vertex(vertex)
        self._vertexes.append(vertexobj) 
    
    def createEdges(self, edgePair):
        for i in range(len(self._vertexes)):
            if(edgePair[0] == self._vertexes[i]._value):
                fromvertex = self._vertexes[i]
                break
        for j in range(len(self._vertexes)):
            if(edgePair[1] == self._vertexes[j]._value):
                tovertex = self._vertexes[j]
                self._vertexes[i]._adjacent_vertexes.append(self._vertexes[j])
                break
        if(len(edgePair) == 3):
            self._edges.append(Edge(fromvertex,tovertex,edgePair[2])) 
        else:
            self._edges.append(Edge(fromvertex,tovertex))        
    
    def prim(self,initialVertex):
        queue = list(self._vertexes)
        primsEdges = []
        caVk = 0
        for vrtxs in queue:
            if vrtxs._value == initialVertex:
                initialVertex = vrtxs
        initialVertex._distVertex = 0
        initialVertex._prevVertex = None
        vi = initialVertex
        # while i haven´t visited all nodes
        while queue != []:
            minCa = float("inf")
            # Finf minimum Ca
            #print "\n"
            for vrtx in queue:
                #print vrtx._value
                if vrtx._distVertex < minCa:
                    vi = vrtx
                    minCa = vrtx._distVertex
            vi._visited = True
            queue.remove(vi)
            for vk in vi._adjacent_vertexes:
                if vk._visited == False:
                    # get cost from vi to vk
                    for edge in self._edges:
                            if((edge._from == vi) and (edge._to == vk)):
                                caVk = edge._weight
                            elif((edge._from == vk) and (edge._to == vi)):
                                caVk = edge._weight
                    if vk._distVertex > caVk:
                        vk._distVertex = caVk
                        vk._prevVertex = vi
        for vrtx in self._vertexes:
            if vrtx._prevVertex != None:
                primsEdges.append((vrtx._value,vrtx._prevVertex._value))
        return primsEdges
                
class Vertex:
    """
    Simple vertex Class.
    """
    def __init__(self, value):
        self._value = value
        self._adjacent_vertexes = []
        self._visited = False
        self._prevVertex = None
        self._distVertex = float("inf")

    def __str__(self):
        """
        Return human readable state
        """
        return "Class Vertex: 		"+"\n" \
              +"Value:	"+str(self._value)+"\n" \
              +"Adjacent vertexes:		"+str(self._adjacent_vertexes)+"\n" \
              +"Visited state:  "+str(self._visited)+"\n" \
              +"prev Vertex: "+str(self._prevVertex)+"\n" \
              +"dist Vertex: "+str(self._distVertex)+"\n"
    # functions of the Vertex Class                              
    def get_adjacent_vertexes(self):        
        return self._adjacent_vertexes
    def insert_adj_vertex(self, vertex_adj_cls):
        self._adjacent_vertexes.append(vertex_adj_cls)    
    def visited(self):
        self._visited = True
    def unvisited(self):
        self._visited = False
    def setPrevVertex(self, vertexRef):
        self._prevVertex = vertexRef
    def setDistVertex(self, value):
        self._distVertex = value
        
class Vertex_ref:
    """
    Simple Adjacent Vertex Class.
    """
    # This just generate a variable which points to the vertex class
    def __init__(self, vertex):
        self._vertexRef = vertex

    def __str__(self):
        """
        Return human readable state
        """
        return "Class Adjacent vertex:		"+"\n" \
              +"vertexRef Val:	"+str(self._vertexRef)+"\n"         
        
class Edge:
    """
    Simple Edge Class.
    """
    def __init__(self, fromvertex, tovertex, weight=0): 
        self._from = fromvertex
        self._to = tovertex
        self._weight = weight

print "Graph nodes\n"
print data
print "\nGraph edges\n"
print edges
AGraph = Graph(data, edges)
print "\nThe Graph\n"
print AGraph
initVertex = "v1"
print "\nEdges of Prim´s-MST\n"
PrimsEdges = AGraph.prim(initVertex)
print PrimsEdges

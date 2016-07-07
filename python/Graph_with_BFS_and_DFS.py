#Graph implementation by Francisco Eduardo Balart Sanchez
# imports
import math
import random

data = [0, 1, 2, 3, 4, 5]
edges = [[0,1],[0,4],[0,5],[1,4],[1,3],[2,1],[3,4],[3,2]]

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
        self._edges.append(Edge(fromvertex,tovertex))        
        
    # Breath First Search Algorithm
    def bfs(self, initialVertex):
        queue = []
        path = []
        currentVertex = None
        for vrtxs in self._vertexes:
            if vrtxs._value == initialVertex:
                initialVertex = vrtxs
        # enqueue the first vertex provided
        queue.append(initialVertex)
        path.append(initialVertex._value)
        initialVertex._visited = True
        # BFS Algorithm
        while queue != []:
            # dequeue
            currentVertexRef = queue.pop(0)
            for adjvrtx in currentVertexRef.get_adjacent_vertexes():
                if adjvrtx._visited == False:
                    path.append(adjvrtx._value)
                    adjvrtx._visited = True
                    queue.append(adjvrtx)
        print "The BFS from vertex "+str(initialVertex._value)+" is:\n"
        return path
       
    # Depth First Search Algorithm
    def dfs(self, initialVertex):
        stack = []
        path = []
        curentVertex = None
        for vrtxs in self._vertexes:
            if vrtxs._value == initialVertex:
                initialVertex = vrtxs
        # put in the stack the initial vertex
        print "pushing to stack"
        print initialVertex._value
        stack.append(initialVertex)
        path.append(initialVertex._value)
        initialVertex._visited = True
        # DFS Algorithm
        while stack != []:
            # pop
            currentVertexRef = stack.pop()
            if currentVertexRef._visited == False:
                currentVertexRef._visited = True
                path.append(currentVertexRef._value)
            for adjvrtx in currentVertexRef.get_adjacent_vertexes():
                if adjvrtx._visited == False:                                        
                    stack.append(adjvrtx)
                    print "pushing to stack"
                    print adjvrtx._value
        return path
    
class Vertex:
    """
    Simple vertex Class.
    """
    def __init__(self, value):
        self._value = value
        self._adjacent_vertexes = []
        self._visited = False

    def __str__(self):
        """
        Return human readable state
        """
        return "Class Vertex: 		"+"\n" \
              +"Value:	"+str(self._value)+"\n" \
              +"Adjacent vertexes:		"+str(self._adjacent_vertexes)+"\n" \
              +"Visited state:  "+str(self._visited)+"\n"
    # functions of the Vertex Class                              
    def get_adjacent_vertexes(self):        
        return self._adjacent_vertexes
    def insert_adj_vertex(self, vertex_adj_cls):
        self._adjacent_vertexes.append(vertex_adj_cls)    
    def visited(self):
        self._visited = True
    def unvisited(self):
        self._visited = False
        
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
        
class Edge():
    """
    Simple Edge Class.
    """
    def __init__(self, fromvertex, tovertex): 
        self._from = fromvertex
        self._to = tovertex


print "Graph nodes\n"
print data
print "Graph edges\n"
print edges
AGraph = Graph(data, edges)
print "The Graph\n"
print AGraph
#print "BFS of the Graph starting node 0\n"
#print AGraph.bfs(0)
print "\n"
print "DFS of the Graph starting node 0\n"
print AGraph.dfs(0)

#Graph implementation by Francisco Eduardo Balart Sanchez
# imports
import math
import random

#data = [0, 1, 2, 3, 4, 5]
#edges = [[0,1],[0,4],[0,5],[1,4],[1,3],[2,1],[3,4],[3,2]]
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
    
    # Dijkstra
    def dijkstra(self, initialVertex):
        #initialize
        for vrtxs in self._vertexes:
            if vrtxs._value == initialVertex:
                initialVertex = vrtxs
        initialVertex._distVertex = 0
        stack = []
        queue = list(self._vertexes)
        # algorithm start here
        while(queue != []):
            #find min in existing vertex of queue
            uVertex = queue[0]
            for vrtx in queue:
                if(vrtx._distVertex < uVertex._distVertex):
                    uVertex = vrtx
            # we add to the stakc minimum d[v]
            stack.append(uVertex)
            queue.remove(uVertex)
            uVertex._visited = True
            for vrtx in uVertex._adjacent_vertexes:
                if vrtx._visited == False:
                    # we need to know the weight of the edge from uVertex to Vrtx
                    for edge in self._edges:
                        if((edge._from == uVertex) and (edge._to == vrtx)):
                            weightUV = edge._weight
                    if((uVertex._distVertex+weightUV)<vrtx._distVertex):
                        vrtx._prevVertex = uVertex
                        vrtx._distVertex = uVertex._distVertex+weightUV
        return stack                
                   
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
#print "BFS of the Graph starting node 0\n"
#print AGraph.bfs(0)
print "\n"
#print "DFS of the Graph starting node 0\n"
#print AGraph.dfs(0)
destnode = "v6"
initvrtx = "v1"
print "Dijkstra of the Graph starting at node v1 \n"
dijstack = AGraph.dijkstra(initvrtx)
dijstackcopy = list(dijstack)
print dijstackcopy
print "\nfinal stack is\n"
while(dijstack!=[]):
    print dijstack.pop()._value
print "\nshortest path from node "+str(initvrtx)+" to node "+str(destnode)+"\n"
found = False
shortest_path = []
currentVrtx = dijstackcopy.pop()
prevNode=currentVrtx._prevVertex
while(dijstackcopy!=[]):
    if currentVrtx._value == destnode:
        shortest_path.append(currentVrtx._value)
        prevNode = currentVrtx._prevVertex
        currentVrtx = dijstackcopy.pop() 
        continue
    if currentVrtx._value == prevNode._value:
        shortest_path.append(currentVrtx._value)
        prevNode = currentVrtx._prevVertex
    if(currentVrtx._value == initvrtx):
        shortest_path.append(currentVrtx._value)
    if(prevNode._value == initvrtx):
        shortest_path.append(prevNode._value)
    currentVrtx = dijstackcopy.pop() 
    
print shortest_path

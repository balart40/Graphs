package febalart_graphs_pkg;

import java.util.ArrayList;
import java.util.LinkedList;

public class Graph_class_vI {

	protected ArrayList <vertexClass> vertexes;
	protected ArrayList <edgeClass> edges;
	
	public Graph_class_vI(LinkedList<String> data, LinkedList<LinkedList<String>> edges){
		this.vertexes = new ArrayList<vertexClass>();
		this.edges = new ArrayList<edgeClass>();
		for (String vrtx : data){
			insertVertex(vrtx);
		}
		for (LinkedList<String> edge: edges){
			createEdges(edge);
		}
	}
	
	
    public void insertVertex(String vertex) {
    	vertexClass vertexobj;
        vertexobj = new vertexClass(vertex);
        this.vertexes.add(vertexobj);
    }
    
    public void createEdges(LinkedList<String> edgePair){
    	vertexClass fromvertex = null;
    	vertexClass tovertex = null;
    	//System.out.println("from before =  "+fromvertex.value);
    	for(int i=0; i<this.vertexes.size(); i++ )
    	{
    		if(edgePair.get(0) == this.vertexes.get(i).value)
    		{
    			fromvertex = this.vertexes.get(i);
    			break;
    		}			
    	}
    	for(int j=0; j<this.vertexes.size(); j++ )
    	{
    		if(edgePair.get(1) == this.vertexes.get(j).value)
    		{
    			tovertex = this.vertexes.get(j);
    			break;
    		}
    	}
    	fromvertex.adjacentVertexes.add(tovertex);
    	edgeClass edgeobj = new edgeClass(fromvertex, tovertex);
    	this.edges.add(edgeobj);
    }
    
    public LinkedList<String> bfs(String initialVertex){
    	LinkedList<String> path = new LinkedList<String>();;
    	LinkedList<vertexClass>  queue = new LinkedList<vertexClass>();
    	vertexClass currentVertex;
    	vertexClass initialVertexObj = null;
    	for(vertexClass vrtxs : this.vertexes)
    	{
    		if(vrtxs.value == initialVertex)
    		{
    			initialVertexObj = vrtxs;
    		}
    	}
    	queue.add(initialVertexObj);
    	path.add(initialVertexObj.value);
    	initialVertexObj.visited = true;
    	// BFS Algorithm
    	//System.out.println(queue);
    	while(!queue.isEmpty())
    	{
    		currentVertex = queue.get(0);
    		queue.remove(0);
    		for(vertexClass adjvrtx : currentVertex.adjacentVertexes)
    		{
    			if(adjvrtx.visited == false)
    			{
    				path.add(adjvrtx.value);
    				adjvrtx.visited = true;
    				queue.add(adjvrtx);
    			}
    		}
    	}
    	
    	return path;
    }
    
    
    
}

import java.util.ArrayList;

public class vertexClass {
	
	protected String value;
	protected ArrayList <vertexClass> adjacentVertexes; 
	protected Boolean visited;
	
	public vertexClass(String value){
		this.value = value;
		this.adjacentVertexes = new ArrayList<vertexClass>();
		this.visited = false;
	}
	
	public String toString(){
		return "Class Vertex\nValue: "+this.value+"\nAdjacent vertexes: "+this.adjacentVertexes+"\nVisited: "+this.visited;
	}
	
}

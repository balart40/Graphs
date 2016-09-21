package febalart_graphs_pkg;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class GraphSimulation {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
				
		/*LinkedList<String> data = new LinkedList<String>(Arrays.asList("v1", "v2", "v3", "v4", "v5", "v6", "v7"));
		LinkedList<LinkedList<String>> edges = new LinkedList<LinkedList<String>>();
		edges.add(new LinkedList<String>(Arrays.asList("v1","v2")));
		edges.add(new LinkedList<String>(Arrays.asList("v1","v4")));
		edges.add(new LinkedList<String>(Arrays.asList("v2", "v4")));
		edges.add(new LinkedList<String>(Arrays.asList("v2", "v5")));
		edges.add(new LinkedList<String>(Arrays.asList("v5", "v7")));
		edges.add(new LinkedList<String>(Arrays.asList("v7", "v6")));
		edges.add(new LinkedList<String>(Arrays.asList("v3", "v1")));
		edges.add(new LinkedList<String>(Arrays.asList("v3", "v6")));
		edges.add(new LinkedList<String>(Arrays.asList("v4", "v3")));
		edges.add(new LinkedList<String>(Arrays.asList("v4", "v6")));
		edges.add(new LinkedList<String>(Arrays.asList("v4", "v7")));
		edges.add(new LinkedList<String>(Arrays.asList("v4", "v5")));
		*/
		LinkedList<String> data = new LinkedList<String>(Arrays.asList("v0", "v1", "v2", "v3", "v4", "v5"));
		LinkedList<LinkedList<String>> edges = new LinkedList<LinkedList<String>>();
		edges.add(new LinkedList<String>(Arrays.asList("v0","v1")));
		edges.add(new LinkedList<String>(Arrays.asList("v0","v4")));
		edges.add(new LinkedList<String>(Arrays.asList("v0","v5")));
		edges.add(new LinkedList<String>(Arrays.asList("v1","v4")));
		edges.add(new LinkedList<String>(Arrays.asList("v1","v3")));
		edges.add(new LinkedList<String>(Arrays.asList("v2","v1")));
		edges.add(new LinkedList<String>(Arrays.asList("v3","v4")));
		edges.add(new LinkedList<String>(Arrays.asList("v3","v2")));
		
		String initialVertex = "v0";
		LinkedList<String> bfspathofgraph;
		
		Graph_class_vI AGraph = new Graph_class_vI(data, edges);
		bfspathofgraph = AGraph.bfs(initialVertex);
		System.out.println(bfspathofgraph);
	}

}

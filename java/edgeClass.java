public class edgeClass {

	protected vertex from;
	protected vertex to;

	public edgeClass(vertex fromVertex, vertex toVertex){
		this.from = fromVertex;
		this.to = toVertex;
	}

	public String toString() {
		return "Class Edge\nFrom: " + this.from + "To: " + this.to;
	}

}

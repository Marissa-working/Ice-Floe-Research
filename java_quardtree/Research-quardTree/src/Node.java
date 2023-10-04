import java.util.List;

public class Node {
    float x0;
    float y0;
    float width;
    List<Node> children;
    List<Node> parent;
    int id;

    Node(float x0, float y0, float width, List<Node> children, List<Node> parent, int id) {
        this.x0 = x0;
        this.y0 = y0;
        this.width = width;
        this.children = children;
        this.parent = parent;
        this.id = id;
    }
}

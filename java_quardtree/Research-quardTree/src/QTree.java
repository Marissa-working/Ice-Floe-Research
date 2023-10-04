import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.lang.Math;

public class QTree {
    Node root;
    List<Node> leafListCopy;
    List<Node> leafList;
    List<Node> parentList;
    Map<Float, Integer> sizeDist;
    int maxDivison = 20;
    int maxWidth = 1000;

    QTree() {
        this.root = new Node(0, 0, maxWidth, new ArrayList<>(), null, UUID.randomUUID().hashCode() & 0xffff);
        this.leafList = new ArrayList<>();
        this.leafList.add(this.root);
        this.leafListCopy = new ArrayList<>();
        this.leafListCopy.add(this.root);
        this.parentList = new ArrayList<>();
        // Create additional layers with divisions
        int numInitialLayers = 9; // Number of layers to create
        int numDivided = 3; // Number of floes to subdivide

        Node currentNode = this.root;
        createLayers(currentNode, numInitialLayers, numDivided);
        for (Node a : leafList) {
            System.out.println("Node ID: " + a.id);
        }

    }

    private void createLayers(Node currentNode, int totalLayers, int numDivided) {
        // Base case: Stop recursion when we reach the desired number of layers
        if (totalLayers <= 0) {
            System.out.println(currentNode.id);
            return;
        }
        subdivide(currentNode);
        for (int j = 0; j < numDivided; j++) {
            subdivide(currentNode.children.get(j));
            createLayers(currentNode.children.get(j),totalLayers -1,numDivided);
        }


    }

    void subdivide(Node node) {
        float w_ = node.width / 2.0f;
        Node x1 = new Node(node.x0, node.y0,  w_, new ArrayList<>(), List.of(node), UUID.randomUUID().hashCode() & 0xffff);
        Node x2 = new Node(node.x0, node.y0 +  w_,  w_, new ArrayList<>(), List.of(node), UUID.randomUUID().hashCode() & 0xffff);
        Node x3 = new Node(node.x0 + w_, node.y0,  w_, new ArrayList<>(), List.of(node), UUID.randomUUID().hashCode() & 0xffff);
        Node x4 = new Node(node.x0 +  w_, node.y0 +  w_, w_, new ArrayList<>(), List.of(node), UUID.randomUUID().hashCode() & 0xffff);
        node.children.add(x1);
        node.children.add(x2);
        node.children.add(x3);
        node.children.add(x4);
        this.leafList.remove(node);
        this.leafListCopy.remove(node);
        if (countDivisions(w_) >= this.maxDivison){
            if (node.parent != null && node.parent.get(0) != null ) {
                this.parentList.remove(node.parent.get(0));
            }
            this.parentList.add(node);
            this.leafListCopy.add(x1);
            this.leafListCopy.add(x2);
            this.leafListCopy.add(x3);
            this.leafListCopy.add(x4);
            return;
        }
        this.leafList.add(x1);
        this.leafList.add(x2);
        this.leafList.add(x3);
        this.leafList.add(x4);
        this.leafListCopy.add(x1);
        this.leafListCopy.add(x2);
        this.leafListCopy.add(x3);
        this.leafListCopy.add(x4);
        if (node.parent != null && node.parent.get(0) != null ) {
            this.parentList.remove(node.parent.get(0));
        }

        this.parentList.add(node);
    }

    void weld(Node node) {
        this.parentList.remove(node);
        this.leafList.remove(node.children.get(0));
        this.leafList.remove(node.children.get(1));
        this.leafList.remove(node.children.get(2));
        this.leafList.remove(node.children.get(3));
        this.leafList.add(node);

        this.leafListCopy.remove(node.children.get(0));
        this.leafListCopy.remove(node.children.get(1));
        this.leafListCopy.remove(node.children.get(2));
        this.leafListCopy.remove(node.children.get(3));
        this.leafListCopy.add(node);

        if (node.parent != null && node.parent.get(0) != null ) {
            if(node.parent.get(0).children.size() == 0) {
                System.out.println(node.parent.get(0).x0 + " "+node.parent.get(0).y0 + " "+ node.x0 + " "+ node.y0);
            }else{
                if (this.leafListCopy.contains(node.parent.get(0).children.get(0))
                        && this.leafListCopy.contains(node.parent.get(0).children.get(1))
                        && this.leafListCopy.contains(node.parent.get(0).children.get(2))
                        && this.leafListCopy.contains(node.parent.get(0).children.get(3))) {
                    this.parentList.add(node.parent.get(0));
                }
            }
        }
        node.children.clear();
    }

    int countDivisions(double x) {
        double base = 2.0;
        double num = Math.log(1000.0 / x) / Math.log(base);
        return (int) Math.round(num);
    }

    List<Node> getLeaves() {
        return this.leafList;
    }

    List<Node> getParent() {
        return this.parentList;
    }

    void updateSizeDist() {
        this.sizeDist = new HashMap<Float, Integer>();
        List<Node> leaves = this.leafListCopy;
        for (Node item : leaves) {
            if (item != null) {
                if (!this.sizeDist.containsKey(item.width)) {
                    this.sizeDist.put( item.width, 1);
                } else {
                    this.sizeDist.put(item.width, this.sizeDist.get(item.width) + 1);
                }
            }
        }
    }
    void plotSizeDistribution() {
        this.sizeDist = new HashMap<Float, Integer>();
        updateSizeDist();
        List<Float> sizes = new ArrayList<>(this.sizeDist.keySet());
        sizes.sort(null);
        List<Integer> counts = new ArrayList<>();
        for (float size : sizes) {
            counts.add(this.sizeDist.get(size));
        }
        System.out.println("sizes: " + sizes);
        System.out.println("counts: " + counts);
        // Code for plotting the graph using a suitable Java plotting library goes here.
    }


}

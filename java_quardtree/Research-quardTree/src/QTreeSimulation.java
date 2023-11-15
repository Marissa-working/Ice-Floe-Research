import java.util.List;
import java.util.Random;
import java.util.ArrayList;
public class QTreeSimulation {

    private static Random random = new Random();
    private static boolean error = false;
    public static void case_0(QTree quard) {
        // nothing happens
    }

    public static void case_1(QTree quard) {
        // divide
        List<Node> leafList = quard.getLeaves();
        if(leafList.size() == 0){
            return;
        }
        Node node = leafList.get(random.nextInt(leafList.size()));
        quard.subdivide(node);
    }

    public static void case_2(QTree quard) {
        if (quard.getParent().size() == 1 || quard.getParent().isEmpty()) {
            return;
        }
        // weld
        List<Node> parentList = quard.getParent();
        Node node = parentList.get(random.nextInt(parentList.size()));
        if(quard.weld(node)){
            error =  true;
        };
    }

    private static QTree createLayers(QTree quard, Node currentNode, int totalLayers, int numDivided) {
        // Base case: Stop recursion when we reach the desired number of layers
        if (totalLayers <= 0) {
            return quard;
        }
        quard.subdivide(currentNode);
        for (int j = 0; j < numDivided; j++) {
            //quard.subdivide(currentNode.children.get(j));
            //printTree(quard);
            createLayers(quard, currentNode.children.get(j), totalLayers - 1, numDivided);
        }
        return quard;
    }
    public static QTree setup(QTree quard, int num){
        Node current = quard.root;
        quard = createLayers(quard, current, num, 3);
        return quard;
    }
    // 0: nothing happens
    // 1: fracture
    // 2: weld
    public static QTree splitWeldSimulate(double splitRate, double weldRate, int seconds) {
        QTree quardExample = setup(new QTree(), 6);

//        QTree quardExample =new QTree();
//        quardExample.subdivide(quardExample.root);
//        quardExample.subdivide(quardExample.root.children.get(0));
//        quardExample.subdivide(quardExample.root.children.get(1));
//        quardExample.subdivide(quardExample.root.children.get(2));
//        quardExample.subdivide(quardExample.root.children.get(0).children.get(0).children.get(0));
        //printTree(quardExample);

        if (splitRate + weldRate > 1) {
            System.out.println("Error: invalid input, probability sum larger than 1");
            return null;
        }
        double nothingRate = 1 - splitRate - weldRate;
        double[] weights = {nothingRate, splitRate, weldRate};
        ArrayList<Integer> numList = new ArrayList<>();
        Runnable[] behaviors = {() -> case_0(quardExample), () -> case_1(quardExample), () -> case_2(quardExample)};
        for (int i = 0; i < 10000 * seconds; i++) {
            if(error){
                System.out.println("error run time " +i);
                break;
            }
            // after each 5000 runs, print size distribution
            if(i % 5000 == 0){
                numList.add(quardExample.leafListCopy.size());
            }

            // get which interval it falls: 0: nothing happens; 1: fracture; 2: weld
            int index = getRandomWeightedIndex(weights);
            behaviors[index].run();
            //printTree(quardExample);
        }
        // after run 10000*seconds times, plot and print the size distribution
        quardExample.plotSizeDistribution();
        System.out.println("numFloes: " + numList);
        //printTree(quardExample);
        return quardExample;
    }

    private static int getRandomWeightedIndex(double[] weights) {
        // generate a random float between 0 and 1
        double randomValue = random.nextDouble();
        double cumulativeProbability = 0;
        // check which interval the random number falls in
        for (int i = 0; i < weights.length; i++) {
            cumulativeProbability += weights[i];
            if (randomValue <= cumulativeProbability) {
                return i;
            }
        }
        return weights.length - 1; // Fallback if something goes wrong (should not happen).
    }

    public static void printTree(QTree qtree) {
        printTreeRecursive(qtree.root, 0);
        System.out.println("children id: ");
        for (Node child : qtree.leafListCopy) {
            System.out.print(child.id + ", ");
        }
        System.out.println();
        System.out.println("parent id: ");
        for (Node child : qtree.parentList) {
            System.out.print(child.id+ ", ");
        }
        System.out.println();
    }

    private static void printTreeRecursive(Node node, int level) {
        if (node == null) {
            return;
        }

        // Print the current node's ID with indentation based on its level
        StringBuilder indent = new StringBuilder();
        for (int i = 0; i < level; i++) {
            indent.append("  "); // Two spaces for each level
        }
        System.out.println(indent + "Level " + level + ": Node ID " + node.id);

        // Recursively print the children nodes
        for (Node child : node.children) {
            printTreeRecursive(child, level + 1);
        }
    }

}


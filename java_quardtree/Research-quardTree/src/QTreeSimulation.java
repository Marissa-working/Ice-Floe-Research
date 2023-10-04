import java.util.List;
import java.util.Random;
import java.util.ArrayList;
public class QTreeSimulation {

    private static Random random = new Random();

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
        quard.weld(node);
    }

    // 0: nothing happens
    // 1: fracture
    // 2: weld
    public static QTree splitWeldSimulate(double splitRate, double weldRate, int seconds) {
        QTree quardExample = new QTree();
        if (splitRate + weldRate > 1) {
            System.out.println("Error: invalid input, probability sum larger than 1");
            return null;
        }
        double nothingRate = 1 - splitRate - weldRate;
        double[] weights = {nothingRate, splitRate, weldRate};
        ArrayList<Integer> numList = new ArrayList<>();
        Runnable[] behaviors = {() -> case_0(quardExample), () -> case_1(quardExample), () -> case_2(quardExample)};
        for (int i = 0; i < 10000 * seconds; i++) {
            if(i % 5000 == 0){
                numList.add(quardExample.leafListCopy.size());
            }
            int index = getRandomWeightedIndex(weights);
            behaviors[index].run();
        }
        quardExample.plotSizeDistribution();
        System.out.println("numFloes: " + numList);
        return quardExample;
    }

    private static int getRandomWeightedIndex(double[] weights) {
        double randomValue = random.nextDouble();
        double cumulativeProbability = 0;
        for (int i = 0; i < weights.length; i++) {
            cumulativeProbability += weights[i];
            if (randomValue <= cumulativeProbability) {
                return i;
            }
        }
        return weights.length - 1; // Fallback if something goes wrong (should not happen).
    }
}


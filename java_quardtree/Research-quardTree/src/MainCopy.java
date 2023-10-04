import com.google.gson.Gson;
import java.io.FileWriter;
import java.io.File;
import java.io.IOException;
import java.util.*;

public class MainCopy {
    public static void main(String[] args) {
        // Pass: Test.test1();
        double splitRate;
        double weldRate;
        int seconds;
        List<Map<String, Double>> nodeData;
        String fileName;
        File existingFile;

        // Case 7.1:(0.3, 0.1, 50)
        System.out.println("Case 7.1: splitRate = 0.3, weldRate = 0.1, times = 500,000");
        splitRate = 0.3;
        weldRate = 0.1;
        seconds = 50;
        QTree qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        nodeData = new ArrayList<>();
        for (Node node : qTree.leafListCopy) {
            Map<String, Double> nodeInfo = new HashMap<>();
            nodeInfo.put("x0", (double) node.x0);
            nodeInfo.put("y0", (double) node.y0);
            nodeInfo.put("width", (double) node.width);
            nodeData.add(nodeInfo);
        }
        // Specify the file name
       fileName = "leaf7.1.json";

        // Delete the existing file if it exists
        existingFile = new File(fileName);
        if (existingFile.exists()) {
            existingFile.delete();
        }

        // Write new data to the file
        try (FileWriter writer = new FileWriter(fileName)) {
            new Gson().toJson(nodeData, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println();

        // Case 7.2:(0.5, 0.1, 50)
        System.out.println("Case 7.2: splitRate = 0.5, weldRate = 0.1, times = 500,000");
        splitRate = 0.5;
        weldRate = 0.1;
        seconds = 50;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        nodeData = new ArrayList<>();
        for (Node node : qTree.leafListCopy) {
            Map<String, Double> nodeInfo = new HashMap<>();
            nodeInfo.put("x0", (double) node.x0);
            nodeInfo.put("y0", (double) node.y0);
            nodeInfo.put("width", (double) node.width);
            nodeData.add(nodeInfo);
        }
        // Specify the file name
        fileName = "leaf7.2.json";

        // Delete the existing file if it exists
        existingFile = new File(fileName);
        if (existingFile.exists()) {
            existingFile.delete();
        }

        // Write new data to the file
        try (FileWriter writer = new FileWriter(fileName)) {
            new Gson().toJson(nodeData, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println();

        // Case 7.3:(0.7, 0.1, 50)
        System.out.println("Case 7.3: splitRate = 0.7, weldRate = 0.1, times = 500,000");
        splitRate = 0.7;
        weldRate = 0.1;
        seconds = 50;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        nodeData = new ArrayList<>();
        for (Node node : qTree.leafListCopy) {
            Map<String, Double> nodeInfo = new HashMap<>();
            nodeInfo.put("x0", (double) node.x0);
            nodeInfo.put("y0", (double) node.y0);
            nodeInfo.put("width", (double) node.width);
            nodeData.add(nodeInfo);
        }
        // Specify the file name
        fileName = "leaf7.3.json";

        // Delete the existing file if it exists
        existingFile = new File(fileName);
        if (existingFile.exists()) {
            existingFile.delete();
        }

        // Write new data to the file
        try (FileWriter writer = new FileWriter(fileName)) {
            new Gson().toJson(nodeData, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println();

        // Case 7.4:(0.9, 0.1, 50)
        System.out.println("Case 7.4: splitRate = 0.9, weldRate = 0.1, times = 500,000");
        splitRate = 0.9;
        weldRate = 0.1;
        seconds = 50;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        nodeData = new ArrayList<>();
        for (Node node : qTree.leafListCopy) {
            Map<String, Double> nodeInfo = new HashMap<>();
            nodeInfo.put("x0", (double) node.x0);
            nodeInfo.put("y0", (double) node.y0);
            nodeInfo.put("width", (double) node.width);
            nodeData.add(nodeInfo);
        }
        // Specify the file name
        fileName = "leaf7.4.json";

        // Delete the existing file if it exists
        existingFile = new File(fileName);
        if (existingFile.exists()) {
            existingFile.delete();
        }

        // Write new data to the file
        try (FileWriter writer = new FileWriter(fileName)) {
            new Gson().toJson(nodeData, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println();



        // Test: just divide once
//        QTree quard = new QTree();
//        List<Node> leafList = quard.getLeaves();
//        Random random = new Random();
//        Node node = leafList.get(random.nextInt(leafList.size()));
//        quard.subdivide(node);
//        quard.plotSizeDistribution();
//        QTreeVisualization visualization = new QTreeVisualization("Quadtree Visualization", quard);
//        visualization.displayGraph();
    }

}

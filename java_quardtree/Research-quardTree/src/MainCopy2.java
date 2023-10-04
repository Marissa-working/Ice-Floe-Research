import com.google.gson.Gson;

import javax.swing.*;
import java.io.FileWriter;
import java.io.File;
import java.io.IOException;
import java.util.*;

public class MainCopy2 {
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
        // Specify the file name
        fileName = "leaf7.2.csv";

        // Delete the existing file if it exists
        existingFile = new File(fileName);
        if (existingFile.exists()) {
            existingFile.delete();
        }

        // Write new data to the file
        try (FileWriter writer = new FileWriter(fileName)) {
            for (Node node : qTree.leafListCopy) {
                writer.write(node.x0 + "," + node.y0 + "," + node.width + "\n");
            }
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
        fileName = "leaf7.3.csv";

        // Delete the existing file if it exists
        existingFile = new File(fileName);
        if (existingFile.exists()) {
            existingFile.delete();
        }

        // Write new data to the file
        try (FileWriter writer = new FileWriter(fileName)) {
            for (Node node : qTree.leafListCopy) {
                writer.write(node.x0 + "," + node.y0 + "," + node.width + "\n");
            }
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
        fileName = "leaf7.4.csv";

        // Delete the existing file if it exists
        existingFile = new File(fileName);
        if (existingFile.exists()) {
            existingFile.delete();
        }

        // Write new data to the file
        try (FileWriter writer = new FileWriter(fileName)) {
            for (Node node : qTree.leafListCopy) {
                writer.write(node.x0 + "," + node.y0 + "," + node.width + "\n");
            }
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

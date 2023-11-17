import javax.swing.*;
import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Main {
    public static JFrame displayFrame(QTree qTree) {
        JFrame frame = new JFrame("Square Drawing Example");
        frame.add(new SquareDrawingExample(qTree));
        frame.setSize(800, 800);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        return frame;
    }

    private static void rectangleData(QTree qTree){
        float rate = (float) (800.0/(float)qTree.maxWidth);
        List<Node> leafListCopy = qTree.leafListCopy;
        List<List<Float>> nodeListValues = new ArrayList<>();
        for (Node node : leafListCopy) {
            float width = (float) node.width * rate;
            float x0 = (float) node.x0 * rate;
            float y0 = (float) node.y0 * rate;
            if (x0 > 800 || y0 > 800 || y0 < 0 || x0 < 0) {
                System.out.println("error: out of bound " + x0 + " " + y0 + " " + width);
            }
            List<Float> nodeValues = new ArrayList<>();
            nodeValues.add(width);
            nodeValues.add(x0);
            nodeValues.add(y0);

            // Add the list to the main list
            nodeListValues.add(nodeValues);
        }
        System.out.println("nodeListValues = " + nodeListValues);
        //return nodeListValues;
    }
    public static void main(String[] args) {
        double splitRate;
        double weldRate;
        int seconds;
        QTree qTree;
        JFrame frame;
        BufferedImage image;

        // Case 9.1:(0.7, 0.2, 500) 15 maxDivison setup = 6
        splitRate = Double.parseDouble(args[0]);
        weldRate = Double.parseDouble(args[1]);
        seconds = Integer.parseInt(args[2]);;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        //rectangleData(qTree);

        System.out.println();
    }


}

import javax.swing.*;
import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.List;
import java.util.Random;

public class Main {
    private static JFrame displayFrame(QTree qTree) {
        JFrame frame = new JFrame("Square Drawing Example");
        frame.add(new SquareDrawingExample(qTree));
        frame.setSize(800, 800);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        return frame;
    }


    public static void main(String[] args) {
        // Pass: Test.test1();
        double splitRate;
        double weldRate;
        int seconds;
        QTree qTree;
        JFrame frame;
        BufferedImage image;

        // Test pass: just divide once
        QTree quard = new QTree();
        List<Node> leafList = quard.getLeaves();
        Random random = new Random();
        Node node = leafList.get(random.nextInt(leafList.size()));
        //quard.subdivide(node);
        displayFrame(quard);
//
//        // Test pass:  divide twice, merge once
//        quard = new QTree();
//        leafList = quard.getLeaves();
//        random = new Random();
//        node = leafList.get(random.nextInt(leafList.size()));
//        quard.subdivide(node);
//        node = leafList.get(random.nextInt(leafList.size()));
//        quard.subdivide(node);
//        displayFrame(quard);
//        List<Node> parentList = quard.getParent();
//        node = parentList.get(random.nextInt(parentList.size()));
//        quard.weld(node);
//        displayFrame(quard);
//        node = parentList.get(random.nextInt(parentList.size()));
//        quard.weld(node);
//        displayFrame(quard);

//        // Case 7.1:(0.3, 0.1, 50)
//        System.out.println("Case 7.1: splitRate = 0.3, weldRate = 0.1, times = 500,000");
//        splitRate = 0.3;
//        weldRate = 0.1;
//        seconds = 50;
//        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
//        // Display the frame and get the JFrame instance
//        frame = displayFrame(qTree);
//
//        // Capture the content of the panel as an image
//        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
//        frame.paint(image.getGraphics());
//
//        // Save the image as a PNG file
//        try {
//            ImageIO.write(image, "PNG", new File("drawing7.1maxDivison20.png"));
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
//
//        System.out.println();
//
//        // Case 7.2:(0.5, 0.1, 50)
//        System.out.println("Case 7.2: splitRate = 0.5, weldRate = 0.1, times = 500,000");
//        splitRate = 0.5;
//        weldRate = 0.1;
//        seconds = 50;
//        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
//        // Display the frame and get the JFrame instance
//        frame = displayFrame(qTree);
//
//        // Capture the content of the panel as an image
//        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
//        frame.paint(image.getGraphics());
//
//        // Save the image as a PNG file
//        try {
//            ImageIO.write(image, "PNG", new File("drawing7.2maxDivison20.png"));
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
//        System.out.println();
//
//        // Case 7.3:(0.7, 0.1, 50)
//        System.out.println("Case 7.3: splitRate = 0.7, weldRate = 0.1, times = 500,000");
//        splitRate = 0.7;
//        weldRate = 0.1;
//        seconds = 50;
//        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
//        // Display the frame and get the JFrame instance
//        frame = displayFrame(qTree);
//
//        // Capture the content of the panel as an image
//        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
//        frame.paint(image.getGraphics());
//
//        // Save the image as a PNG file
//        try {
//            ImageIO.write(image, "PNG", new File("drawing7.3maxDivison20.png"));
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
//        System.out.println();
//
//        // Case 7.4:(0.9, 0.1, 50)
//        System.out.println("Case 7.4: splitRate = 0.9, weldRate = 0.1, times = 500,000");
//        splitRate = 0.9;
//        weldRate = 0.1;
//        seconds = 50;
//        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
//        // Display the frame and get the JFrame instance
//        frame = displayFrame(qTree);
//
//        // Capture the content of the panel as an image
//        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
//        frame.paint(image.getGraphics());
//
//        // Save the image as a PNG file
//        try {
//            ImageIO.write(image, "PNG", new File("drawing7.4maxDivison20.png"));
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
//        System.out.println();
//
//    }
//
//
    }
}

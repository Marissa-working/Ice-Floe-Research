import javax.swing.*;
import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
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


    public static void main(String[] args) {
        // Pass: Test.test1();
        double splitRate;
        double weldRate;
        int seconds;
        QTree qTree;
        JFrame frame;
        BufferedImage image;

        // Case 9.1:(0.7, 0.2, 500) 15 maxDivison setup = 6
        splitRate = 0.7;
        weldRate = 0.2;
        seconds = 500;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        // Display the frame and get the JFrame instance
        frame = displayFrame(qTree);

        // Capture the content of the panel as an image
        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
        frame.paint(image.getGraphics());

        // Save the image as a PNG file
        try {
            ImageIO.write(image, "PNG", new File("drawing9.1.png"));
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println();

        // Case 9.2:(0.7, 0.2, 5000) 15 maxDivison setup = 6
        splitRate = 0.7;
        weldRate = 0.2;
        seconds = 5000;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        // Display the frame and get the JFrame instance
        frame = displayFrame(qTree);

        // Capture the content of the panel as an image
        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
        frame.paint(image.getGraphics());

        // Save the image as a PNG file
        try {
            ImageIO.write(image, "PNG", new File("drawing9.2.png"));
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println();

        // Case 9.3:(0.7, 0.2, 6000) 15 maxDivison setup = 6
        splitRate = 0.7;
        weldRate = 0.2;
        seconds = 6000;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        // Display the frame and get the JFrame instance
        frame = displayFrame(qTree);

        // Capture the content of the panel as an image
        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
        frame.paint(image.getGraphics());

        // Save the image as a PNG file
        try {
            ImageIO.write(image, "PNG", new File("drawing9.3.png"));
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println();


        // Case 9.4:(0.7, 0.2, 7000) 15 maxDivison setup = 6
        splitRate = 0.7;
        weldRate = 0.2;
        seconds = 7000;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        // Display the frame and get the JFrame instance
        frame = displayFrame(qTree);

        // Capture the content of the panel as an image
        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
        frame.paint(image.getGraphics());

        // Save the image as a PNG file
        try {
            ImageIO.write(image, "PNG", new File("drawing9.4.png"));
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println();

        // Case 9.5:(0.7, 0.2, 8000) 15 maxDivison setup = 6
        splitRate = 0.7;
        weldRate = 0.2;
        seconds = 8000;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        // Display the frame and get the JFrame instance
        frame = displayFrame(qTree);

        // Capture the content of the panel as an image
        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
        frame.paint(image.getGraphics());

        // Save the image as a PNG file
        try {
            ImageIO.write(image, "PNG", new File("drawing9.5.png"));
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println();

        // Case 9.6:(0.7, 0.2, 50000) 15 maxDivison setup = 6
        splitRate = 0.7;
        weldRate = 0.2;
        seconds = 9000;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        // Display the frame and get the JFrame instance
        frame = displayFrame(qTree);

        // Capture the content of the panel as an image
        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
        frame.paint(image.getGraphics());

        // Save the image as a PNG file
        try {
            ImageIO.write(image, "PNG", new File("drawing9.6.png"));
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println();

        // Case 9.7:(0.7, 0.2, 50000) 15 maxDivison setup = 6
        splitRate = 0.7;
        weldRate = 0.2;
        seconds = 10000;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        // Display the frame and get the JFrame instance
        frame = displayFrame(qTree);

        // Capture the content of the panel as an image
        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
        frame.paint(image.getGraphics());

        // Save the image as a PNG file
        try {
            ImageIO.write(image, "PNG", new File("drawing9.7.png"));
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println();

        // Case 9.8:(0.7, 0.2, 50000) 15 maxDivison setup = 6
        splitRate = 0.7;
        weldRate = 0.2;
        seconds = 50000;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        // Display the frame and get the JFrame instance
        frame = displayFrame(qTree);

        // Capture the content of the panel as an image
        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
        frame.paint(image.getGraphics());

        // Save the image as a PNG file
        try {
            ImageIO.write(image, "PNG", new File("drawing9.8.png"));
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println();

        // Case 9.9:(0.7, 0.2, 60000) 15 maxDivison setup = 6
        splitRate = 0.7;
        weldRate = 0.2;
        seconds = 60000;
        qTree = QTreeSimulation.splitWeldSimulate(splitRate, weldRate, seconds);
        // Display the frame and get the JFrame instance
        frame = displayFrame(qTree);

        // Capture the content of the panel as an image
        image = new BufferedImage(800, 800, BufferedImage.TYPE_INT_RGB);
        frame.paint(image.getGraphics());

        // Save the image as a PNG file
        try {
            ImageIO.write(image, "PNG", new File("drawing9.9.png"));
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println();

    }


}

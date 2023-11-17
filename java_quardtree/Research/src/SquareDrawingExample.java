import javax.swing.*;
import java.awt.*;
import java.awt.geom.Rectangle2D;
import java.util.List;

public class SquareDrawingExample extends JPanel {

    private final QTree qTree;

    public SquareDrawingExample(QTree qTree) {
        this.qTree = qTree;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        float rate = (float) (800.0/(float)this.qTree.maxWidth);
        List<Node> leafListCopy = qTree.leafListCopy;
        for (Node node : leafListCopy) {
            float width = (float) node.width * rate;
            float x0 = (float) node.x0 * rate;
            float y0 = (float) node.y0 * rate;
            if(x0 >800 || y0>800 || y0 < 0 || x0<0){
                System.out.println(x0 +" " + y0 + " "+ width);
            }
            //System.out.println(x0 +" " + y0 + " "+ width);
            Rectangle2D.Float rect = new Rectangle2D.Float(x0, y0, width, width);
            g2d.draw(rect);
        }
        //System.out.println("end");
    }
}

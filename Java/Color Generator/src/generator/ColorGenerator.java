package generator;

import javax.swing.JFrame;
import javax.swing.JPanel;

import java.awt.*;


class DrawPanel extends JPanel {
	private static final long serialVersionUID = 1L;

	public int r = (int)(Math.random()*256);
	public int g = (int)(Math.random()*256);
	public int b = (int)(Math.random()*256);
	public Color random = new Color(r,g,b);
	
	private void draw(Graphics g) {
        
		g.setColor(random);
		g.fillRect(0, 0, (int)(Double.POSITIVE_INFINITY), (int)(Double.POSITIVE_INFINITY));
		
		
		Color textColor = Color.BLACK;
        int darkness = 0;
        if(this.r<125)
            darkness++;
        if(this.g<125)
            darkness++;
        if(this.b<125)
            darkness++;
        if(darkness>=2){
        	textColor = Color.WHITE;
        }
        Font textFont = new Font("Comic Sans",Font.BOLD,100); 
        Font textFont2 = new Font("Comic Sans",Font.BOLD,50); 
        
        g.setColor(textColor);
        g.setFont(textFont);
        //g.drawString(RGBToHex.convertRGBtoHex(this.r,this.g,this.b), 1080/2-250, 100);
        g.drawString(RGBToHex.convertRGBtoHex(this.r,this.g,this.b), 20, 100);
        g.setFont(textFont2);
        g.drawString("("+this.r+","+this.g+","+this.b+")", 450, 100);
		
    }


    @Override
    public void paintComponent(Graphics g) {

        super.paintComponent(g);
        draw(g);
    }
}

public class ColorGenerator extends JFrame {
	private static final long serialVersionUID = 1L;

public ColorGenerator() {

      initUI();
  }

  private void initUI() {

      DrawPanel drawPanel = new DrawPanel();
      add(drawPanel);
      setSize(1080, 1080);
      setTitle("Color");
      setLocationRelativeTo(null);
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  }

  public static void main(String[] args) {

      EventQueue.invokeLater(() -> {
    	  ColorGenerator ex = new ColorGenerator();
          ex.setVisible(true);
      });
  }
}
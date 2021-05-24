package Runner;

import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.*;


class DrawPanel extends JPanel {
	
	int frame = (int)(Math.random()*121);
	int red = (int)(Math.random()*256);
    int green = (int)(Math.random()*256);
    int blue = (int)(Math.random()*256);
	String batteryInt = ((int)(Math.random()*11)+45)+"%";
	
    private void draw(Graphics g) {
        //Create objects in this method
        
        if(frame == 72 || frame == 71 || frame == 73 || frame == 74 || frame == 70)
            frame = 255; //White if matching background
        Color frameColor = new Color(frame,frame,frame); //Random Frame
	    Color wallpaperColor = new Color(red,green,blue); //Random Wallpaper
	    
        IPhone iphone = new IPhone(g, frameColor, wallpaperColor, batteryInt); //Passing frame color and wallpaper color
        
    }


    //DONT TOUCH THIS NEITHER!
    @Override
    public void paintComponent(Graphics g) {

        super.paintComponent(g);
        draw(g);
    }
}


//Create Classes here V

//Super Class
class Device {
    public Device(Graphics g, Color frameColor, Color wallpaperColor){
        //Background
        int threshold1 = 200;
        int threshold2 = 100;
        int threshold3 = 100;
        int threshold4 = 75;
        int backgroundR;
        int backgroundG;
        int backgroundB;
        
        //Background based on chosen wallpaper
        backgroundR = wallpaperColor.getRed() + threshold1;
        backgroundG = wallpaperColor.getGreen() + threshold1;
        backgroundB = wallpaperColor.getBlue() + threshold1;
        if(Math.max(Math.max(backgroundR,backgroundG),backgroundB)>255){
            backgroundR = wallpaperColor.getRed() + threshold2;
            backgroundG = wallpaperColor.getGreen() + threshold2;
            backgroundB = wallpaperColor.getBlue() + threshold2;
            if(Math.max(Math.max(backgroundR,backgroundG),backgroundB)>255){
                backgroundR = wallpaperColor.getRed() - threshold3;
                backgroundG = wallpaperColor.getGreen() - threshold3;
                backgroundB = wallpaperColor.getBlue() - threshold3;
                if(Math.min(Math.min(backgroundR,backgroundG),backgroundB)<0){
                    backgroundR = wallpaperColor.getRed() - threshold4;
                    backgroundG = wallpaperColor.getGreen() - threshold4;
                    backgroundB = wallpaperColor.getBlue() - threshold4;
                    if(Math.min(Math.min(backgroundR,backgroundG),backgroundB)<0){
                        backgroundR = 72;
                        backgroundG = 72;
                        backgroundB = 72;
                    }
                }
            }
        }
        g.setColor(new Color(backgroundR,backgroundG,backgroundB));
        g.fillRect(0,0,250,400);
        
        //Frame parts
        g.setColor(frameColor);
        g.fillOval(10,10,10,10);
        g.fillOval(250-20,10,10,10);
        g.fillOval(10,400-20,10,10);
        g.fillOval(250-20,400-20,10,10);
        
        g.fillRect(15,10,250-20-10,380);
        g.fillRect(10,15,250-20,370);
        
    }
}

//Super-Sub Class (Phone is a Device)
class Phone extends Device {
    public Phone(Graphics g, Color frameColor, Color wallpaperColor){
        super(g, frameColor, wallpaperColor); //Passing frame color and wallpaper color
        
        //Screen parts(Wallpaper)
        g.setColor(wallpaperColor);
        g.fillOval(10+5,10+5,10,10);
        g.fillOval(250-20-5,10+5,10,10);
        g.fillOval(10+5,400-20-5,10,10);
        g.fillOval(250-20-5,400-20-5,10,10);
        
        g.fillRect(20,15,250-20-5-15,370);
        g.fillRect(15,20,250-20-10,360);
        
    }
}

//Subclass (IPhone is a Phone)
class IPhone extends Phone {
    //IPhone has Apps
    Apps a;
    
    public IPhone(Graphics g, Color frameColor, Color wallpaperColor, String batteryInt){
        super(g, frameColor, wallpaperColor); //Passing frame color and wallpaper color
        
        //Change UI color based on background color for visibility
        Color overlay = Color.BLACK;
        Color batteryText = Color.YELLOW;
        int darkness = 0;
        if(wallpaperColor.getRed()<125)
            darkness++;
        if(wallpaperColor.getGreen()<125)
            darkness++;
        if(wallpaperColor.getBlue()<125)
            darkness++;
        if(darkness>=2){
            overlay = Color.WHITE;
            batteryText = new Color (207, 191, 19);
        }
        
        //UI Parts
        //Notch
        g.setColor(Color.BLACK);
        g.fillRect(125-40,15,80,20);
        //g.drawArc has x,y,width,height,starting point,degrees traveled
        g.fillArc(125-40-20,-5,40,40,180,90);
        g.fillArc(145,-5,40,40,270,90);
        
        //Dock
        Color overlayClear = new Color(overlay.getRed(),overlay.getGreen(),overlay.getBlue(),50);
        g.setColor(overlayClear);
        Polygon dock = new Polygon();
        //Top L
        //dock.addPoint(20,330); //Pointed Corner
        dock.addPoint(20,335);
        dock.addPoint(21,331);
        dock.addPoint(25,330);
        //Top R
        //dock.addPoint(230,330); //Pointed Corner
        dock.addPoint(225,330);
        dock.addPoint(229,331);
        dock.addPoint(230,335);
        //Bot R
        //dock.addPoint(230,380); //Pointed Corner
        dock.addPoint(230,375);
        dock.addPoint(229,379);
        dock.addPoint(225,380);
        //Bot L
        //dock.addPoint(20,380); //Pointed Corner
        dock.addPoint(25,380);
        dock.addPoint(21,379);
        dock.addPoint(20,375);
        g.fillPolygon(dock);
        
        //Pages
        g.setColor(overlay);
        g.fillOval(125-13,320,7,7);
        g.setColor(overlayClear);
        g.fillOval(125-3,320,7,7);
        g.fillOval(125+7,320,7,7);
        
        //Time
        g.setColor(overlay);
        Font time = new Font("Comic Sans",Font.BOLD,10); 
        g.setFont(time);
        g.drawString("10:09",25,30); //"Standard" watch time
        
        //Battery
        g.setColor(batteryText);
        g.fillRect(195,20,15,10);
        g.setColor(overlay);
        g.drawRect(195,20,30,10);
        Font battery = new Font("Comic Sans",Font.BOLD,7); 
        g.setFont(battery);
        g.drawString(batteryInt,201,28);
        
        //Apps
        a = new Apps(g);
    }
}

//Composition Class (IPhone has Apps)
class Apps {
    public Apps(Graphics g){
        Safari(g);
        Calendar(g);
        Weather(g);
        Mail(g);
        Messages(g);
        Webex(g);
        FindMy(g);
        Notes(g);
        Google(g);
    }
    //Methods for each app
    public void AppFrame(Graphics g, Color c, int x, int y){
        g.setColor(c);
        //40x40, 15 spacing
        g.fillOval(x, y, 20, 20);
        g.fillOval(x+20, y, 20, 20);
        g.fillOval(x, y+20, 20, 20);
        g.fillOval(x+20, y+20, 20, 20);
        
        g.fillRect(x+10,y,20,40);
        g.fillRect(x,y+10,40,20);
    }
    //20, 40 1, 1
    //75, 40 2, 1
    //130, 40 3, 1
    //185, 40 4, 1
    
    //20, 95 1, 2
    //75, 95 2, 2
    //130, 95 3, 2
    //185, 95 4, 2
    
    //20, 150 1, 3
    //75, 150 2, 3
    //130, 150 3, 3
    //185, 150 4, 3
    
    //50, 335 Dock 1
    //105, 335 Dock 2
    //160, 335 Dock 3
    public void Safari(Graphics g){
        //Dock 1
        int posX = 50;
        int posY = 335;
        AppFrame(g, new Color(254, 254, 254), posX, posY);
        
        g.setColor(new Color(29, 159, 245));
        g.fillOval(posX+4, posY+4, 32, 32);
        g.setColor(new Color(133, 226, 253));
        g.drawOval(posX+6, posY+6, 28, 28);
        g.setColor(new Color(254, 58, 47));
        Polygon redTriangle = new Polygon();
        redTriangle.addPoint(posX+30,posY+7);
        redTriangle.addPoint(posX+30-12,posY+7+10);
        redTriangle.addPoint(posX+30-6,posY+7+14);
        g.fillPolygon(redTriangle);
        g.setColor(new Color(254, 254, 254));
        Polygon whiteTriangle = new Polygon();
        whiteTriangle.addPoint(posX+30-12,posY+7+10);
        whiteTriangle.addPoint(posX+30-6,posY+7+14);
        whiteTriangle.addPoint(posX+30-22,posY+7+12+12+2);
        g.fillPolygon(whiteTriangle);
    }
    public void Calendar(Graphics g){
        //1,1 
        int posX = 20;
        int posY = 40;
        AppFrame(g, new Color(254, 254, 254), posX, posY);
        
        g.setColor(new Color(254, 59, 58));
        Font day = new Font("Comic Sans",Font.BOLD,8); 
        g.setFont(day);
        g.drawString("WED", posX+10, posY+13);
        g.setColor(new Color(38, 38, 38));
        Font date = new Font("Comic Sans",Font.PLAIN,20); 
        g.setFont(date);
        g.drawString("21", posX+8, posY+33);
    }
    public void Weather(Graphics g){
        //2,1
        int posX = 75;
        int posY = 40;
        AppFrame(g, new Color(27,160,247), posX, posY);
        
        g.setColor(new Color(255, 204, 0));
        g.fillOval(posX+7,posY+7,15,15);
        g.setColor(new Color(227, 243, 254));
        g.fillOval(posX+10,posY+20,12,12);
        g.fillOval(posX+20,posY+17,15,15);
        g.fillOval(posX+15,posY+13,15,15);
        g.fillRect(posX+20,posY+28,10,4);
    }
    public void Mail(Graphics g){
        //Dock 3
        int posX = 160;
        int posY = 335;
        AppFrame(g, new Color(27,159,247), posX, posY);
        
        g.setColor(new Color(254, 254, 254));
        g.fillOval(posX+5, posY+10, 10, 10);
        g.fillOval(posX+5, posY+20, 10, 10);
        g.fillOval(posX+25, posY+10, 10, 10);
        g.fillOval(posX+25, posY+20, 10, 10);
        g.fillRect(posX+10, posY+10, 20, 20);
        g.fillRect(posX+5, posY+15, 30, 10);
        
        g.setColor(new Color(27,159,247));
        g.drawLine(posX+5, posY+10, posX+20, posY+20);
        g.drawLine(posX+35, posY+10, posX+20, posY+20);
        
        g.drawLine(posX+5, posY+25, posX+15, posY+18);
        g.drawLine(posX+35, posY+25, posX+25, posY+18);
    }
    public void Messages(Graphics g){
        //Dock 2
        int posX = 105;
        int posY = 335;
        AppFrame(g, new Color(77,236,104), posX, posY);
        
        g.setColor(new Color(254, 254, 254));
        g.fillOval(posX+5, posY+7, 30, 22);
        Polygon bubble = new Polygon();
        bubble.addPoint(posX+12, posY+24);
        bubble.addPoint(posX+16, posY+27);
        bubble.addPoint(posX+6, posY+32);
        g.fillPolygon(bubble);
    }
    public void Webex(Graphics g){
        //1, 2
        int posX = 20;
        int posY = 95;
        AppFrame(g, new Color(254,254,254), posX, posY);
        
        g.setColor(new Color(0, 80, 114));
        g.fillArc(posX+5, posY+5, 30, 30, 230, 180);
        g.setColor(new Color(110, 190, 74));
        g.fillOval(posX+10, posY+10, 20, 20);
        g.setColor(new Color(0, 188, 235));
        g.fillArc(posX+5, posY+5, 30, 30, 230-180, 180);
        g.setColor(new Color(254,254,254));
        g.fillOval(posX+10, posY+10, 17, 17);
    }
    public void FindMy(Graphics g){
        //4, 1
        int posX = 185;
        int posY = 40;
        AppFrame(g, new Color(219,220,218), posX, posY);
        
        g.setColor(new Color(54, 206, 98));
        g.fillOval(posX+5, posY+5, 30, 30);
        g.setColor(new Color(5, 122, 233));
        g.fillArc(posX+5, posY+5, 30, 30, 60, 60);
        g.setColor(new Color(86, 221, 113));
        g.drawOval(posX+12, posY+12, 15, 15);
        g.setColor(new Color(239, 239, 244));
        g.fillOval(posX+15, posY+15, 10, 10);
        g.setColor(new Color(0, 122, 255));
        g.fillOval(posX+17, posY+17, 6, 6);
    }
    public void Notes(Graphics g){
        //3, 1
        int posX = 130;
        int posY = 40;
        AppFrame(g, new Color(254,254,254), posX, posY);
        
        g.setColor(new Color(255, 211, 36));
        g.fillOval(posX, posY, 20, 20);
        g.fillOval(posX+20, posY, 20, 20);
        g.fillRect(posX+10,posY,20,20);
        g.setColor(new Color(254,254,254));
        g.fillRect(posX,posY+10,40,20);
        g.setColor(new Color(209,209,212));
        g.drawLine(posX, posY+17, posX+39, posY+17);
        g.drawLine(posX, posY+27, posX+39, posY+27);
    }
    public void Google(Graphics g){
        //2, 2
        int posX = 75;
        int posY = 95;
        AppFrame(g, new Color(254,254,254), posX, posY);
        
        g.setColor(new Color(234, 67, 53)); //Red
        g.fillArc(posX+5, posY+5, 30, 30, 50, 100);
        g.setColor(new Color(251, 188, 5)); //Yellow
        g.fillArc(posX+5, posY+5, 30, 30, 50+100, 50);
        g.setColor(new Color(52, 168, 83)); //Green
        g.fillArc(posX+5, posY+5, 30, 30, 50+100+50, 110);
        g.setColor(new Color(66, 133, 244)); //Blue
        g.fillArc(posX+5, posY+5, 30, 30, 360-50, 50);
        g.setColor(new Color(254,254,254));
        g.fillOval(posX+10, posY+10, 20, 20);
        g.setColor(new Color(66, 133, 244)); //Blue
        g.fillRect(posX+23,posY+20,10,4);
    }
}


//DO NOT CHANGE ANYTHING DOWN HERE!
public class Runner extends JFrame {

    public Runner() {

        initUI();
    }

    private void initUI() {

        DrawPanel drawPanel = new DrawPanel();
        add(drawPanel);

        setSize(250, 400);
        setTitle("Graphics");
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public static void main(String[] args) {

        EventQueue.invokeLater(() -> {
            Runner ex = new Runner();
            ex.setVisible(true);
        });
    }
}
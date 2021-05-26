package games;

public class Slots {

	public String slots[] = {"C", "S", "B", "O", "K", "W"};
	//public String slots[] = {"🍒", "🍓", "🍌", "🍊", "🥝", "🍉"};
	public String slot1;
	public String slot2;
	public String slot3;
	
	public void playSlots() {
		runSlots();
		testWin();
	}
	
	public void runSlots() {
		slot1 = slots[(int)(Math.random()*slots.length)];
		slot2 = slots[(int)(Math.random()*slots.length)];
		slot3 = slots[(int)(Math.random()*slots.length)];
		System.out.println("Rolling 1st slot: "+slot1);
		System.out.println("Rolling 2nd slot: "+slot2);
		System.out.println("Rolling 3rd slot: "+slot3);
		System.out.println("\nSlots: "+slot1+slot2+slot3);
	}
	
	public void testWin() {
		if(slot1.equalsIgnoreCase(slot2) && slot2.equalsIgnoreCase(slot3)) {
			System.out.println("You win, slots match!");
		} else System.out.println("You lose!");
	}
}

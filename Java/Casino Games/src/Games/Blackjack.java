package Games;
import java.util.Scanner;

public class Blackjack {

	public int playSum;
	public int compSum;
	public int[] playHand = new int[25];
	public int[] compHand = new int[25];
	public int playCurrentIndex;
	public int compCurrentIndex;
	public boolean playHit = true;
	public boolean compHit = true;
	String temp = "";
	
	public void playBlackjack() {
		Scanner key = new Scanner(System.in);
		startGame();
		if(getPlaySum()<=21) System.out.print("Player turn: ");
		while(playHit && getPlaySum()<=21) {
		System.out.print("\nEnter \"hit\" to get another card: ");
		String hit = key.nextLine();
		if(hit.equalsIgnoreCase("hit")){
			playCurrentIndex++;
			playHand[playCurrentIndex] = genCard();
			System.out.println("\nPlayer Hand: "+getPlayHand());
			System.out.println("Total: "+getPlaySum());
			playBust();
			} else {
				playHit = false;
				System.out.println("Player will stay");
			}
		}
		if(getPlaySum()<=21) {
			System.out.println("\nDealer's turn: ");
			System.out.println("\nDealer Hand: "+getCompHand());
			System.out.println("Total: "+getCompSum());
			while(getCompSum()<17) {
				if(getCompSum()<17) {
					compCurrentIndex++;
					compHand[compCurrentIndex] = genCard();
					System.out.println("\nDealer Hand: "+getCompHand());
					System.out.println("Total: "+getCompSum());
					compBust();
				} 
			}
			if(getCompSum()<=21) {
				System.out.println("Dealer stays");
				testWin();
			}
		
		}
	}
	
	public int genCard() {
		int[] cards = {11,2,3,4,5,6,7,8,9,10,10,10,10};
		return cards[(int)(Math.random()*cards.length)];
	}
	public void startGame() {
		System.out.println("Player dealt two cards");
		playHand[0] = genCard();
		playHand[1] = genCard();
		playCurrentIndex  = 1;
		System.out.println("Player Hand: "+getPlayHand());
		System.out.println("Total: "+getPlaySum());
		System.out.println("\nDealer dealt two cards, one hidden");
		compHand[0] = genCard();
		compHand[1] = genCard();
		compCurrentIndex = 1;
		System.out.println("Dealer Hand: "+compHand[0]+"\n");
		playBust();
	}
	public String getPlayHand() {
		temp = "";
		for(int i = 0; i < playHand.length; i++) {
			if(playHand[i] != 0) {
				temp += playHand[i]+" ";
			}
		}
		return temp;
	}
	public String getCompHand() {
		temp = "";
		for(int i = 0; i < compHand.length; i++) {
			if(compHand[i] != 0) {
				temp += compHand[i]+" ";
			}
		}
		return temp;
	}
	public int getPlaySum() {
		playSum = 0;
		for(int i = 0; i < playHand.length; i++) {
			playSum += playHand[i];
		}
		return playSum;
	}
	public int getCompSum() {
		compSum = 0;
		for(int i = 0; i < compHand.length; i++) {
			compSum += compHand[i];
		}
		return compSum;
	}
	public void playBust() {
		if(getPlaySum()>21) {
			System.out.println("Player busts! You lose!");
		}
	}
	public void compBust() {
		if(getCompSum()>21) {
			System.out.println("Dealer busts! You win!");
		}
	}
	public void testWin() {
		if(getPlaySum()<=21) {
			if(getCompSum()<=21) {
				if(getCompSum()>getPlaySum()) {
					System.out.println("\nYou lose! "+getCompSum()+">"+getPlaySum());
				} else System.out.println("\nYou win! "+getCompSum()+"<"+getPlaySum());
				if(getCompSum()==getPlaySum()) {
					System.out.println("\nYou lose! Dealer and player tie");
			} else compBust();
		} else playBust();
	}
	}
}

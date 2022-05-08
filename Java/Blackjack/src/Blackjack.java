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
	
	public static void main(String[] args) {
		Scanner key = new Scanner(System.in);
		Blackjack game = new Blackjack();
		game.startGame();
		if(game.getPlaySum()<=21) System.out.print("Player turn: ");
		while(game.playHit && game.getPlaySum()<=21) {
		System.out.print("\nEnter \"hit\" to get another card: ");
		String hit = key.nextLine();
		if(hit.equalsIgnoreCase("hit")){
			game.playCurrentIndex++;
			game.playHand[game.playCurrentIndex] = game.genCard();
			System.out.println("\nPlayer Hand: "+game.getPlayHand());
			System.out.println("Total: "+game.getPlaySum());
			game.playBust();
			} else {
				game.playHit = false;
				System.out.println("Player will stay");
			}
		}
		if(game.getPlaySum()<=21) {
			System.out.println("\nDealer's turn: ");
			System.out.println("\nDealer Hand: "+game.getCompHand());
			System.out.println("Total: "+game.getCompSum());
			while(game.getCompSum()<17) {
				if(game.getCompSum()<17) {
					game.compCurrentIndex++;
					game.compHand[game.compCurrentIndex] = game.genCard();
					System.out.println("\nDealer Hand: "+game.getCompHand());
					System.out.println("Total: "+game.getCompSum());
					game.compBust();
				} 
			}
			if(game.getCompSum()<=21) {
				System.out.println("Dealer stays");
				game.testWin();
			}
		
		}
	}
	
	public int genCard() {
		return (int)(Math.random()*10)+2;
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
				if(getCompSum()>=getPlaySum()) {
					System.out.println("\nYou lose!");
				} else System.out.println("\nYou win!");
			} else compBust();
		} else playBust();
	}
}

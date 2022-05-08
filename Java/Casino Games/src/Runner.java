import java.util.*;

public class Runner {
	
	public static void main(String[] args) {
		
		boolean run = true;
		while(run) {
			System.out.println("Select game- blackjack, roulette, slots, baccarat: ");
			@SuppressWarnings("resource")
			Scanner key = new Scanner(System.in);
			String choice = key.nextLine();
			
			if(choice.equalsIgnoreCase("blackjack")) {
				System.out.println("Beginning Blackjack: \n");
				Blackjack game = new Blackjack();
				game.playBlackjack();
			}
			
			if(choice.equalsIgnoreCase("roulette")) {
				System.out.println("Beginning Roulette: \n");
				Roulette game = new Roulette();
				game.playRoulette();
			}
			
			if(choice.equalsIgnoreCase("slots")) {
				System.out.println("Beginning Slots: \n");
				Slots game = new Slots();
				game.playSlots();
			}
			
			if(choice.equalsIgnoreCase("baccarat")) {
				System.out.println("Beginning Baccarat: \n");
				Baccarat game = new Baccarat();
				game.playBaccarat();
			}
			
			System.out.println(); System.out.println();
		}
	}

}

package Games;

import java.util.*;

public class Runner {
	
	public static void main(String[] args) {
		
		boolean run = true;
		while(run) {
			System.out.println("Select game- blackjack: ");
			Scanner key = new Scanner(System.in);
			String choice = key.nextLine();
			
			if(choice.equalsIgnoreCase("blackjack")) {
				System.out.println("Beginning Blackjack: \n");
				Blackjack game = new Blackjack();
				game.playBlackjack();
			}
			System.out.println(); System.out.println();
		}
	}

}

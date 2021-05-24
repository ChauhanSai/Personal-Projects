package games;

import java.util.*;

public class Runner {
	
	public static void main(String[] args) {
		
		boolean run = true;
		while(run) {
			System.out.println("Select game- blackjack, roulette: ");
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
			System.out.println(); System.out.println();
		}
	}

}

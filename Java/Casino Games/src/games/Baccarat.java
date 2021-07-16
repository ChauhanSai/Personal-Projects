package games;
import java.util.Scanner;

public class Baccarat {
	int playerCard1;
	int playerCard2;
	int playerCard3;
	int bankerCard1;
	int bankerCard2;
	int bankerCard3;
	int playerSum;
	int bankerSum;
	
	public void playBaccarat() {
		@SuppressWarnings("resource")
		Scanner key = new Scanner(System.in);
		//Player dealt 1 card
		playerCard1 = genCard();
		playerCard2 = genCard();
		playerSum = getTotal(playerCard1, playerCard2, playerCard3);
		System.out.println("Player dealt a " + playerCard1 + " & " +playerCard2 + " ("+playerSum+")");
		
		//If 8 or 9 player win
		if(playerSum==8 || playerSum==9) {
			System.out.println("Player wins with "+playerSum);
		} else {
			//Banker dealt 1 card
			bankerCard1 = genCard();
			bankerCard2 = genCard();
			bankerSum = getTotal(bankerCard1, bankerCard2, bankerCard3);
			System.out.println("Banker dealt a " + bankerCard1 + " & " +bankerCard2 + " ("+bankerSum+")");
			//Player can hit
			System.out.print("Hit? Y/N : ");
			String playHit = key.next();
			if(playHit.equalsIgnoreCase("Y")) {
				playerCard3 = genCard();
				playerSum = getTotal(playerCard1, playerCard2, playerCard3);
				System.out.println("Player dealt a " + playerCard3 + ", has a " + playerCard1 + " & " +playerCard2 + " ("+playerSum+")");
			}
			playerSum = getTotal(playerCard1, playerCard2, playerCard3);
			bankerSum = getTotal(bankerCard1, bankerCard2, bankerCard3);
			//Banker hit
			if(playHit.equalsIgnoreCase("N")) {
				if(playerSum<=5 && playerSum<7) {
					System.out.println("Banker hits");
					bankerCard3 = genCard();
					bankerSum = getTotal(bankerCard1, bankerCard2, bankerCard3);
					System.out.println("Banker dealt a " + bankerCard3 + ", has a " + bankerCard1 + " & " +bankerCard2 + " ("+bankerSum+")");
				}
			} else {
				if( ((bankerSum<=2 && playerCard3==8) || (bankerSum==3 && playerCard3==8) || (bankerSum==4 && (playerCard3<=7 && playerCard3>=2)) || (bankerSum==5 && (playerCard3<=7 && playerCard3>=4)) || (bankerSum==6 && (playerCard3<=7 && playerCard3>=6))) && playerSum<7 ) {
					System.out.println("Banker hits");
					bankerCard3 = genCard();
					bankerSum = getTotal(bankerCard1, bankerCard2, bankerCard3);
					System.out.println("Banker dealt a " + bankerCard3 + ", has a " + bankerCard1 + " & " +bankerCard2 + " ("+bankerSum+")");
				} 
			} 
			if(bankerCard3 == 0 && playerSum>=bankerSum) {
				System.out.println("Banker hits");
				bankerCard3 = genCard();
				bankerSum = getTotal(bankerCard1, bankerCard2, bankerCard3);
				System.out.println("Banker dealt a " + bankerCard3 + ", has a " + bankerCard1 + " & " +bankerCard2 + " ("+bankerSum+")");
			}
			if(bankerCard3 == 0) System.out.println("Banker does not hit");
			//Tens place removed
			playerSum = getTotal(playerCard1, playerCard2, playerCard3);
			bankerSum = getTotal(bankerCard1, bankerCard2, bankerCard3);
			//Higher number wins
			if(playerSum>=bankerSum) {
				System.out.println("Player wins with a total of "+playerSum);
			} else
				System.out.println("Banker wins with a total of "+bankerSum);
		}
	}
	
	public int genCard() {
		int[] cards = {11,2,3,4,5,6,7,8,9,10,10,10,10};
		return cards[(int)(Math.random()*cards.length)];
	}
	
	public int getTotal(int a, int b, int c) {
		String total = Integer.toString((a+b+c));
		total = String.valueOf(total.charAt(1));
		return Integer.valueOf(total);
	}
}
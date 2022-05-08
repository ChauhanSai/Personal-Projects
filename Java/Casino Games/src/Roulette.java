import java.util.Scanner;

public class Roulette {

	public String[] numberSet = {"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36"};
	public boolean[] a12Set = {true, true, true, true, true, true, true, true, true, true, true, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false}; 
	public boolean[] b12Set = {false, false, false, false, false, false, false, false, false, false, false, false, true, true, true, true, true, true, true, true, true, true, true, true, false, false, false, false, false, false, false, false, false, false, false, false}; 
	public boolean[] c12Set = {false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, true, true, true, true, true, true, true, true, true, true, true, true}; 
	public boolean[] ahalfSet = {true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false}; 
	public boolean[] bhalfSet = {false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true}; 
	public boolean[] evenSet = {false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true}; 
	public boolean[] oddSet = {true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false}; 
	public boolean[] redSet = {true, false, true, false, true, false, true, false, true, false, false, true, false, true, false, true, false, true, true, false, true, false, true, false, true, false, true, false, false, true, false, true, false, true, false, true}; 
	public boolean[] blackSet = {false, true, false, true, false, true, false, true, false, true, true, false, true, false, true, false, true, false, false, true, false, true, false, true, false, true, false, true, true, false, true, false, true, false, true, false}; 
	public boolean[] oSet = {true, true, true, true, true, true, true, true, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false}; 
	public boolean[] ooSet = {false, false, false, false, false, false, false, false, false, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true}; 
	
	public boolean playerHasChosenNum;
	public String playerNum = "0";
	public boolean playerA12;
	public boolean playerB12;
	public boolean playerC12;
	public boolean playerAHalf;
	public boolean playerBHalf;
	public boolean playerEven;
	public boolean playerOdd;
	public boolean playerRed;
	public boolean playerBlack;
	public boolean playerO;
	public boolean playerOO;
	
	public String chosenNum;
	public boolean chosenA12;
	public boolean chosenB12;
	public boolean chosenC12;
	public boolean chosenAHalf;
	public boolean chosenBHalf;
	public boolean chosenEven;
	public boolean chosenOdd;
	public boolean chosenRed;
	public boolean chosenBlack;
	public boolean chosenO;
	public boolean chosenOO;
	
	public void playRoulette() {
		askBet();
		genNumber();
		testWin();
	}
	
	public void askBet() {
		@SuppressWarnings("resource")
		Scanner key = new Scanner(System.in);
		System.out.println("Bet- #, 1st 12, 2nd 12, 3rd 12, 1-18, 19-36, Even, Odd, Red, Black, 0, 00:");
		String playChoice = key.nextLine();
		
		if(playChoice.equalsIgnoreCase("1st 12")) {
			playerA12 = true;
			System.out.println("Player has chosen to bet on 1st 12");
		} else
		if(playChoice.equalsIgnoreCase("2nd 12")) {
			playerB12 = true;
			System.out.println("Player has chosen to bet on 2nd 12");
		} else
		if(playChoice.equalsIgnoreCase("3rd 12")) {
			playerC12 = true;
			System.out.println("Player has chosen to bet on 3rd 12");
		} else
		if(playChoice.equalsIgnoreCase("1-18")) {
			playerAHalf = true;
			System.out.println("Player has chosen to bet on 1-18");
		} else
		if(playChoice.equalsIgnoreCase("19-36")) {
			playerBHalf = true;
			System.out.println("Player has chosen to bet on 19-36");
		} else
		if(playChoice.equalsIgnoreCase("Even")) {
			playerEven = true;
			System.out.println("Player has chosen to bet on Even");
		} else
		if(playChoice.equalsIgnoreCase("Odd")) {
			playerOdd = true;
			System.out.println("Player has chosen to bet on Odd");
		} else
		if(playChoice.equalsIgnoreCase("Red")) {
			playerRed = true;
			System.out.println("Player has chosen to bet on Red");
		} else
		if(playChoice.equalsIgnoreCase("Black")) {
			playerBlack = true;
			System.out.println("Player has chosen to bet on Black");
		} else
		if(playChoice.equalsIgnoreCase("0")) {
			playerO = true;
			System.out.println("Player has chosen to bet on 0");
		} else
		if(playChoice.equalsIgnoreCase("00")) {
			playerOO = true;
			System.out.println("Player has chosen to bet on 00");
		} else {
			playerNum = playChoice;
			playerHasChosenNum = true;
			System.out.println("Player has chosen to bet on "+playerNum);
		}
	}
	
	public void genNumber() {
		int gen = (int)(Math.random()*37);
		chosenNum = numberSet[gen];
		chosenA12 = a12Set[gen];
		chosenB12 = b12Set[gen];
		chosenC12 = c12Set[gen];
		chosenAHalf = ahalfSet[gen];
		chosenBHalf = bhalfSet[gen];
		chosenEven = evenSet[gen];
		chosenOdd = oddSet[gen];
		chosenRed = redSet[gen];
		chosenBlack = blackSet[gen];
		chosenO = oSet[gen];
		chosenOO = ooSet[gen];
		
		String genChoice = chosenNum;
		if(chosenA12) genChoice += ", 1st 12";
		if(chosenB12) genChoice += ", 2nd 12";
		if(chosenC12) genChoice += ", 3rd 12";
		if(chosenAHalf) genChoice += ", 1-18";
		if(chosenBHalf) genChoice += ", 19-36";
		if(chosenEven) genChoice += ", Even";
		if(chosenOdd) genChoice += ", Odd";
		if(chosenRed) genChoice += ", Red";
		if(chosenBlack) genChoice += ", Black";
		if(chosenO) genChoice += ", 0";
		if(chosenOO) genChoice += ", 00";
		System.out.println("\nChosen value: "+genChoice);
	}
	
	public void testWin() {
		if(playerNum.equals(chosenNum) && playerHasChosenNum) {
			win();
			System.out.print(" numbers match!");
		} else
		if(playerA12 && chosenA12) {
			win();
			System.out.print(chosenNum+" is 1st 12!");
		} else
		if(playerB12 && chosenB12) {
			win();
			System.out.print(chosenNum+" is 2nd 12!");
		} else
		if(playerC12 && chosenC12) {
			win();
			System.out.print(chosenNum+" is 3rd 12!");
		} else
		if(playerAHalf && chosenAHalf) {
			win();
			System.out.print(chosenNum+" is 1-18!");
		} else
		if(playerBHalf && chosenBHalf) {
			win();
			System.out.print(chosenNum+" is 19-36!");
		} else
		if(playerEven && chosenEven) {
			win();
			System.out.print(chosenNum+" is Even!");
		} else
		if(playerOdd && chosenOdd) {
			win();
			System.out.print(chosenNum+" is Odd!");
		} else
		if(playerRed && chosenRed) {
			win();
			System.out.print(chosenNum+" is Red!");
		} else
		if(playerBlack && chosenBlack) {
			win();
			System.out.print(chosenNum+" is Black!");
		} else
		if(playerO && chosenO) {
			win();
			System.out.print(chosenNum+" is 0!");
		} else
		if(playerOO && chosenOO) {
			win();
			System.out.print(chosenNum+" is 00!");
		} else lose();
	}
	
	public void win() {
		System.out.print("\nPlayer wins, ");
	}
	public void lose() {
		System.out.print("\nYou lost!");
	}
}

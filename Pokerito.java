import java.util.Random;
import java.util.Scanner;

public class Pokerito{

    public static String randomCard(){
        Random random = new Random();
        int cardNum = random.nextInt(12) + 1;
        switch(cardNum){
            case 1: return "    _____\n" +
            "  |A _  |\n"+ 
            "  | ( ) |\n"+
            "  |(_'_)|\n"+
            "  |  |  |\n"+
            "  |____V|\n";
            case 2: return  "   _____\n"+              
            "  |2    |\n"+ 
            "  |  o  |\n"+
            "  |     |\n"+
            "  |  o  |\n"+
            "  |____Z|\n";
            case 3: return  "   _____\n" +
            "  |3    |\n"+
            "  | o o |\n"+
            "  |     |\n"+
            "  |  o  |\n"+
            "  |____E|\n";
            case 4: return  "   _____\n" +
            "  |4    |\n"+
            "  | o o |\n"+
            "  |     |\n"+
            "  | o o |\n"+
            "  |____h|\n";
            case 5: return "   _____ \n" +
            "  |5    |\n" +
            "  | o o |\n" +
            "  |  o  |\n" +
            "  | o o |\n" +
            "  |____S|\n";
            case 6: return "   _____ \n" +
            "  |6    |\n" +
            "  | o o |\n" +
            "  | o o |\n" +
            "  | o o |\n" +
            "  |____6|\n";
            case 7: return "   _____ \n" +
            "  |7    |\n" +
            "  | o o |\n" +
            "  |o o o|\n" +
            "  | o o |\n" +
            "  |____7|\n";
            case 8: return "   _____ \n" +
            "  |8    |\n" +
            "  |o o o|\n" +
            "  | o o |\n" +
            "  |o o o|\n" +
            "  |____8|\n";
            case 9: return "   _____ \n" +
            "  |9    |\n" +
            "  |o o o|\n" +
            "  |o o o|\n" +
            "  |o o o|\n" +
            "  |____9|\n";
            case 10: return "   _____ \n" +
            "  |10  o|\n" +
            "  |o o o|\n" +
            "  |o o o|\n" +
            "  |o o o|\n" +
            "  |___10|\n";
            case 11: return "   _____\n" +
            "  |J  ww|\n"+ 
            "  | o {)|\n"+ 
            "  |o o% |\n"+ 
            "  | | % |\n"+ 
            "  |__%%[|\n";
            case 12: return "   _____\n" +
            "  |Q  ww|\n"+ 
            "  | o {(|\n"+ 
            "  |o o%%|\n"+ 
            "  | |%%%|\n"+ 
            "  |_%%%O|\n";
            case 13: return "   _____\n" +
            "  |K  WW|\n"+ 
            "  | o {)|\n"+ 
            "  |o o%%|\n"+ 
            "  | |%%%|\n"+ 
            "  |_%%%>|\n";
            default: return "";
        }
    }
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        System.out.print("Let's play Pokerito. Type anything when you're ready.");
        scan.nextLine();
        System.out.println("\nIt's like Poker, but a lot simpler.\n");
        System.out.println("There are two players, you and the computer.\n");
        System.out.println("The dealer will give each player one card.\n");
        System.out.println("Then, the dealer will draw five cards (the river)\n");
        System.out.println("The player with the most river matches wins!\n");
        System.out.println("If the matches are equal, everyone's a winner!\n");
        System.out.print("Ready? Type anything if you are.");
        scan.nextLine();

        // For player
        String PlayerFirstCard = randomCard();
        System.out.println("Here is your first card:\n "+PlayerFirstCard);
        // For computer
        String ComputerFirstCard = randomCard();

        // The river
        String card_1 = randomCard();
        String card_2 = randomCard();
        String card_3 = randomCard();
        String card_4 = randomCard();
        String card_5 = randomCard();
        String dealerCards[] = {card_1, card_2, card_3, card_4, card_5};
        int len = 0;
        int playersMatch = 0;

        // Calculating matched cards for players
        while(len != dealerCards.length){
            if(PlayerFirstCard.equals(dealerCards[len])){
                ++playersMatch;
            }
            ++len;
        }
        int computersMatch = 0;
        int len2 = 0;
        // Calculating matched cards to the computer
        while(len2 != dealerCards.length){
            if(ComputerFirstCard.equals(dealerCards[len2])){
                ++computersMatch;
            }
            ++len2;
        }
        scan.close();
        System.out.println("Here is the computer's first card: ");
        System.out.println(ComputerFirstCard);
        System.out.println("\nHere are the dealer's cards");
        System.out.print(card_1);
        System.out.print(card_3);
        System.out.print(card_2);
        System.out.print(card_4);
        System.out.print(card_5);

        System.out.println("\nYour number of matches: "+playersMatch);
        System.out.println("\nComputer's number of matches: "+computersMatch);

        if(playersMatch > computersMatch){
            System.out.println("You win!");
        }else if(playersMatch < computersMatch){
            System.out.println("Computer wins!");
        }else System.out.println("You both win!");

        
    }
}
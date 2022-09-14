import java.util.Random;
import java.util.Scanner;

public class blackJack{

    public static String randomCards(){
        Random random = new Random();
        int numForCard = random.nextInt(12) + 1;
        switch(numForCard){
            case 1: return "    _____\n" +
            "  |A _  |\n"+ 
            "  | ( ) |\n"+
            "  |(_'_)|\n"+
            "  |  |  |\n"+
            "  |____V|\n";
            case 2: return "   _____\n"+              
            "  |2    |\n"+ 
            "  |  o  |\n"+
            "  |     |\n"+
            "  |  o  |\n"+
            "  |____Z|\n";
            case 3: return "   _____\n" +
            "  |3    |\n"+
            "  | o o |\n"+
            "  |     |\n"+
            "  |  o  |\n"+
            "  |____E|\n";
            case 4: return "   _____\n" +
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
            case 10: return "  _____ \n" +
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
        // creating a function that returns the card value of each card
    }
    public static int cardValue(String card){
        switch(card){
            case "    _____\n" +
            "  |A _  |\n"+ 
            "  | ( ) |\n"+
            "  |(_'_)|\n"+
            "  |  |  |\n"+
            "  |____V|\n":
            return 1;
            case "   _____\n"+              
            "  |2    |\n"+ 
            "  |  o  |\n"+
            "  |     |\n"+
            "  |  o  |\n"+
            "  |____Z|\n":
            return 2;
            case  "   _____\n" +
            "  |3    |\n"+
            "  | o o |\n"+
            "  |     |\n"+
            "  |  o  |\n"+
            "  |____E|\n":
            return 3;
            case "   _____\n" +
            "  |4    |\n"+
            "  | o o |\n"+
            "  |     |\n"+
            "  | o o |\n"+
            "  |____h|\n":
            return 4;
            case "   _____ \n" +
            "  |5    |\n" +
            "  | o o |\n" +
            "  |  o  |\n" +
            "  | o o |\n" +
            "  |____S|\n":
            return 5;
            case "   _____ \n" +
            "  |6    |\n" +
            "  | o o |\n" +
            "  | o o |\n" +
            "  | o o |\n" +
            "  |____6|\n":
            return 6;
            case "   _____ \n" +
            "  |7    |\n" +
            "  | o o |\n" +
            "  |o o o|\n" +
            "  | o o |\n" +
            "  |____7|\n":
            return 7;
            case "   _____ \n" +
            "  |8    |\n" +
            "  |o o o|\n" +
            "  | o o |\n" +
            "  |o o o|\n" +
            "  |____8|\n":
            return 8;
            case "   _____ \n" +
            "  |9    |\n" +
            "  |o o o|\n" +
            "  |o o o|\n" +
            "  |o o o|\n" +
            "  |____9|\n":
            return 9;
            case "  _____ \n" +
            "  |10  o|\n" +
            "  |o o o|\n" +
            "  |o o o|\n" +
            "  |o o o|\n" +
            "  |___10|\n":
            return 10;
            case "   _____\n" +
            "  |J  ww|\n"+ 
            "  | o {)|\n"+ 
            "  |o o% |\n"+ 
            "  | | % |\n"+ 
            "  |__%%[|\n":
            return 10;
            case "   _____\n" +
            "  |Q  ww|\n"+ 
            "  | o {(|\n"+ 
            "  |o o%%|\n"+ 
            "  | |%%%|\n"+ 
            "  |_%%%O|\n":
            return 10;
            case "   _____\n" +
            "  |K  WW|\n"+ 
            "  | o {)|\n"+ 
            "  |o o%%|\n"+ 
            "  | |%%%|\n"+ 
            "  |_%%%>|\n":
            return 10;
            default: return 0;
        
        
        
        }
    }
    public static void main(String args[]){

        Scanner scan = new Scanner(System.in); 
            System.out.println("Welcome to Java Casino!");
            System.out.println("Do you have a Knack for Black Jack?");
            String response = scan.nextLine().toLowerCase();
            if(response.equals("yes")){
                System.out.println("We shall see..");
                System.out.println("Ready? Press anything to begin!");
                scan.nextLine();
            }else System.exit(0);
        
        // I will assign two cards to the players 
        String FirstCardForPlayer = randomCards();
        String SecondCardForPlayer = randomCards();

        String[] CardOfPlayers = {FirstCardForPlayer, SecondCardForPlayer};// list of player's card

        System.out.println("You get a "+CardOfPlayers[0]);
        System.out.println("\nand a "+CardOfPlayers[1]);
        int yourCardValue = cardValue(CardOfPlayers[0]) + cardValue(CardOfPlayers[1]);
        System.out.println("\nYour total is: "+yourCardValue);

        // The dealer's card
        String FirstCardForDealer = randomCards();
        String SecondCardForDealer = randomCards();
        String[] CardOfDealer = {FirstCardForDealer, SecondCardForDealer};
        System.out.println("The dealer shows "+CardOfDealer[0]);
        System.out.println("\nand has a card facing down");
        System.out.println(   "  _______\n"+
                               "|       |\n"+
                               "|   J   |\n"+
                               "|  JJJ  |\n"+
                               "|   J   |\n"+
                               "|_______|");// These is the card facing down
        System.out.println("\nThe dealers total is hidden\n");

        // part two
        while(true){
            String choice = hitOrStay();
            if(choice.equals("hit")){
                String anotherCard = randomCards();
                System.out.println("You get a ");
                System.out.println(anotherCard);
                yourCardValue += cardValue(anotherCard);
                System.out.println("Your total is "+ yourCardValue);
                if(yourCardValue > 21){
                    System.out.println("Bust! Player loses");
                    System.exit(0);
                }else if(yourCardValue < 21){
                    continue;
                }

            }else if(choice.equals("stay")){
                System.out.println("Dealer's turn\n");
                System.out.println("The dealer's cards are ");
                System.out.println(CardOfDealer[0]);
                System.out.println("and ");
                System.out.println(CardOfDealer[1]);
                int dealersTotalCardValue = cardValue(CardOfDealer[0]) + cardValue(CardOfDealer[1]);
                System.out.println("The dealer's total is "+ dealersTotalCardValue);
                while(true){
                    if(dealersTotalCardValue < 17){
                        String dealerNewCard1 = randomCards();

                        System.out.println("The dealer cards is");
                        System.out.println(dealerNewCard1);
                        dealersTotalCardValue += cardValue(dealerNewCard1);
                        System.out.println("Dealer's total is "+ dealersTotalCardValue);
                        continue;

                    }else if(dealersTotalCardValue > 21){
                        System.out.println("Bust! The dealer loses");
                        System.exit(0);
                    }else if((dealersTotalCardValue < 21)&&(dealersTotalCardValue > 17)){
                        System.out.println("The dealer's total is "+ dealersTotalCardValue);
                        System.out.println("Dealer wins!!!");
                        System.exit(0);
                    }
                }

            }
        }

    }    
    // I will create a function that ask to hit or stay
    public static String hitOrStay(){
        Scanner scan = new Scanner(System.in);
        System.out.print("hit or stay: ");
        String response = scan.next();
        while((!response.equals("hit")||(!response.equals("stay")))){
            System.out.print("Please enter 'hit or stay' to continue:");
            response = scan.next();
            if((response.equals("hit")||(response.equals("stay")))){
                break;
            }
        }
        return response;
    }
}
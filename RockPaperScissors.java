import java.util.Scanner;
import java.util.Random;
public class RockPaperScissors{

    public static void main(String args[]){

        Scanner scan = new Scanner(System.in);
        System.out.println("Would you like to play a game of Rock Paper Scissors");
        String response = scan.nextLine().toLowerCase();
        if(response.equals("yes")){
            System.out.println("\nGreat!!!\n");
            System.out.println("When I say shoot, you type in your choice\n");
            System.out.println("rock paper scissors.....shoot!!!\n");

            String yourPick = scan.nextLine().toLowerCase();
            String computerChoice = ComputerChoice();

            if(yourPick.equals(computerChoice)){
                System.out.println("It's a tie");
            }else if((yourPick.equals("rock")&&(computerChoice.equals("paper")))){
                System.out.println("Nice move, you won");
            }else if((yourPick.equals("paper")&&(computerChoice.equals("rock")))){
                System.out.println("I win!!, Well better luck next time");
            }else if((yourPick.equals("rock")&&(computerChoice.equals("scissors")))){
                System.out.println("Nice move, you won");
            }else if((yourPick.equals("scissors")&&(computerChoice.equals("rock")))){
                System.out.println("I win!!, well better luck next time");
            }else if((yourPick.equals("scissors")&&(computerChoice.equals("paper")))){
                System.out.println("Nice move, you won");
            }else if((yourPick.equals("paper")&&(computerChoice.equals("scissors")))){
                System.out.println("I win!!, well better luck next time");
            }else System.out.println("Sorry!!!, will update to include possibility");
            
            System.out.println("Incase your curious I picked "+computerChoice);
        }else
            System.out.println("Darn!!!. Next time I suppose\n");
            System.exit(0);
        scan.close();
    }


    public static String ComputerChoice(){
        int num;
        Random random = new Random();
        num = random.nextInt(3);
        switch(num){
            case 0: return "rock";
            case 1: return "paper";
            case 2: return "scissors";
            default: return " ";
        }
    }
}
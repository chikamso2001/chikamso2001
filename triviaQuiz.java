import java.util.Scanner;
public class triviaQuiz{
    public static void main(String args[]){
        int score = 0;
        Scanner scan = new Scanner(System.in);

        System.out.println("1. Which country held the 2016 summer olympics?");
        System.out.println("a.\tChina \nb.\tIreland \nc.\tBrazil \nd.\tItaly");
        String response1 = scan.nextLine();
        switch(response1){
            case "c": score += 5;break;
            default: score += 0;
        }
        System.out.println("Which planet is the hottest?");
        System.out.println("a.\tVenus \nb.\tSaturn \nc.\tMercury \nd.\tMars");
        String response2 = scan.nextLine();
        switch(response2){
            case "a": score += 5;break;
            default: score += 0;
        }
        System.out.println("What is the rarest blood type?");
        System.out.println("a.\tO \nb.\tA \nc.\tB \nd.\tAB-Negative");
        String response3 = scan.nextLine();
        switch(response3){
            case "d": score += 5;break;
            default: score += 0;
        }
        System.out.println("Which one of these characters is friends with Harry Potter");
        System.out.println("a.\tRon Weasley \nb.\tHermione Granger \nc.\tDraco Malfoy");
        String response4 = scan.nextLine();
        switch(response4){
            case "a": score += 5;break;
            default: score += 0;
        }

        System.out.println("Your final score is "+score);
        
        switch(score){
            case 0: System.out.println("Better luck next time");break;
            case 5: System.out.println("Not Bad!!!");break;
            case 10: System.out.println("Not Bad!!!");break;
            case 15: System.out.println("Wow you really know your stuff!!!");break;
            case 20: System.out.println("You really know your stuff");break; 
            default: break;
        }
        scan.close();
    }
}
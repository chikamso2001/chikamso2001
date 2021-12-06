import java.util.Scanner;
class conditions{
    public static void main(String args[]){
        Scanner Ask_input = new Scanner(System.in);
        System.out.println("Are you feeling happy today?");
        String mood = Ask_input.nextLine();
        String mood1 = mood.toUpperCase();
        if (mood1 == "YES"){
            System.out.println("It's good to see you all jolly today");
        }else{
            System.out.println("Please cheer up, life's hard sometimes");
        }
        Ask_input.close();
    }
}
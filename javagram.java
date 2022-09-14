import java.util.Scanner;

public class javagram{
    public static void main(String args[]){

        System.out.println("Welcome to Javagram, please sign in below");

        String ActUsername = "Chikamso";
        String ActPassword = "94030956Ba";
        Scanner scan = new Scanner(System.in);

        System.out.print("\nUsername: ");
        String username = scan.next();
        System.out.print("Password: ");
        String password = scan.next();

        while((!ActUsername.equals(username))||(!ActPassword.equals(password))){
            System.out.print("\nIncorrect, Please try again!\n");
            System.out.print("Username: ");
            username = scan.next();
            System.out.print("Password: ");
            password = scan.next();
    
        }
        System.out.println("\nSign in Successful. Welcome");
        scan.close();
    }
}

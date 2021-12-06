import java.util.Scanner;
public class gumball{
    static int share;
    public static void main(String args[]){
        Scanner no_of_gumball = new Scanner(System.in);
        Scanner no_of_children = new Scanner(System.in);

        System.out.println("How many gumballs are available:");
        int gumball_number = no_of_gumball.nextInt();

        System.out.println("How many children are present:");
        int children_number = no_of_children.nextInt();

        share = gumball_number/children_number;

        System.out.print("The children should be given ");
        System.out.print(share);
        System.out.println(" each");

        no_of_children.close();
        no_of_gumball.close();
    }
}
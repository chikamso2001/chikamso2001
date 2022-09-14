//Creating a Javapedia program
//Questions asked:
//Name of Historical figure
//Date of birth of figure
//Occupation of figure

import java.util.Scanner;
public class Javapedia{

    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        System.out.println("*********Javapedia********");
        System.out.println("How many historical figures will you register?");
        int numOfHisFig = scan.nextInt();
        scan.nextLine();

        String[][] database = new String[numOfHisFig][3];


        for(int i = 0; i < database.length; ++i){
            System.out.println("Figure "+(i+1));
            System.out.println("Name: ");
            String Name = scan.nextLine();
            database[i][0] = Name;

            System.out.print("Date of Birth: ");
            String DOB = scan.next();
            scan.nextLine();
            database[i][1] = DOB;

            System.out.print("Occupation: ");
            String Occu = scan.next();
            scan.nextLine();
            database[i][2] = Occu;
            System.out.println("\n");

        }
        System.out.println("All information has been stored");
        for(int i = 0; i < database.length; ++i){
            for(int j = 0; j < database[i].length; ++j){
                System.out.print(database[i][j]+"\t");
                if(j == (database[i].length -1)){
                    System.out.println("\n");
                }
            }
        }

        System.out.println("Whose information do you want to look up");
        String theFig = scan.nextLine();

        sortInfo(theFig, database);
        scan.close();
    }

    //Create a function that sorts the database using the name
    public static void sortInfo(String nameOfFig, String[][] database){
        for(int i = 0; i < database.length; ++i){
            if(database[i][0].equals(nameOfFig))
                System.out.println("Name: "+database[i][0]);
                System.out.println("Date of Birth: "+database[i][1]);
                System.out.println("Occupation: "+database[i][2]); break;
            
        }
    }
}
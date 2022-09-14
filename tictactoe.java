import java.util.Scanner;

public class tictactoe{

    public static void main(String args[]){

        Scanner scan = new Scanner(System.in);

        System.out.println("Let's play tic tac toe");
        String[][] theBoard = new String[3][3];
        for(int i = 0; i < theBoard.length; ++i){
            for(int j = 0; j < theBoard[i].length; ++j){
                theBoard[i][j] = "_";
            }
        }
        displayBoard(theBoard);
        System.out.println("\nKnow each player must take turn");

        // Make them take turns in inputing their plays
        for(int i = 0; i < 10; ++i){
            //TODO create a function that checks if there is a winner
            if((i%2) == 0){
                System.out.println("Turn: X");
                System.out.print("Pick a row and column number: ");
                int row = scan.nextInt(); int column = scan.nextInt();
                theBoard = printBoard(row, column, "X",theBoard);
                displayBoard(theBoard);
                scan.nextLine();
            }else if((i%2) == 1){
                System.out.println("Turn: O");
                System.out.print("Pick a row and column number: ");
                int row = scan.nextInt(); int column = scan.nextInt();
                theBoard = printBoard(row, column, "O",theBoard);
                displayBoard(theBoard);
                scan.nextLine();
            }
        }

    }
    //Create a board of 2D Array that stores character
    public static String[][] printBoard(int row, int column, String value, String[][] array){
        Scanner scan = new Scanner(System.in);
        if(array[row][column].equals("_")){
            array[row][column] = value;
        }else{
            //TODO I have to create an exception for inputs outside the boundaries
            while(true){
                System.out.println("Postion is already taken");
                System.out.print("Enter a different position: ");
                row = scan.nextInt(); column = scan.nextInt();
                scan.nextLine();
                if(array[row][column].equals("_")){
                    array[row][column] = value;
                    break;
                }
            }
        }      
        return array;
    }
    //Create a function that displays the board
    public static void displayBoard(String[][] theBoard){
        for(int i = 0; i < theBoard.length; ++i){
            for(int j = 0; j < theBoard[i].length; ++j){
                System.out.print("\t"+theBoard[i][j]+"\t");
                if(j == 2){
                    System.out.print("\n");
                }
            }
        }
    }
    public static void checkWinner(String[][] theArray){
        for(int i = 0; i < theArray.length; ++i){
            
        }
    }
}
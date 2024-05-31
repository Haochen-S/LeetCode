import java.util.Scanner;

public class javaTitleEditor {
    
    public static void main(String[] args) {

        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter leetcode problem title:");

        String title = myObj.nextLine();
        myObj.close();

        String newTitle = "";
        String problemNum = "";
        boolean isProblemNumSet = false;

        int i = 0;
        while (i < title.length()){
            if (!isProblemNumSet) {
                if (title.charAt(i) == '.'){
                    i += 2;
                    isProblemNumSet = true;
                } else {
                    problemNum += title.charAt(i);
                    i++;
                }
                continue;
            }

            if (title.charAt(i) == ' '){
                newTitle += "_";
            }
            else if (title.charAt(i) != '.'){
                newTitle += title.charAt(i);
            }
    
            i += 1;
        }

        newTitle += "_" + problemNum + ".java";
        System.out.println();
        System.out.println(newTitle);
    }
}

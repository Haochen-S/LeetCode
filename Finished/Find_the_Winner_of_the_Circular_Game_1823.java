
import java.util.ArrayList; 
import java.util.List; 

// 1823. Find the Winner of the Circular Game

public class Find_the_Winner_of_the_Circular_Game_1823 {
    
}




class Solution {
    public int findTheWinner(int n, int k) {
        if (n < 2) {
            return 1;
        }
        List<Integer> friendList = new ArrayList<>();
        int i = 1;
        while (i <= n) { 
            friendList.add(i);
            i++;
        }
        System.out.println(friendList.toString());
        
        int start = 0;
        while (n > 1) {
            int leave = k % n;
            leave = (leave + start) % n;
            if (leave == 0) {
                leave = n - 1;
            } else {
                leave--;
            }
            friendList.remove(leave);
            start = leave;
            n--;
            System.out.println(friendList.toString());
        }
        return friendList.get(0);
    }
}
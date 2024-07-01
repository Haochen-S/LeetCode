// 1550. Three Consecutive Odds

public class Three_Consecutive_Odds_1550 {
    
}

class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        if (arr.length < 3) {
            return false;
        }

        int index = 0;
        while (index < arr.length - 2) {
            if (arr[index + 2] % 2 == 0) {
                index += 3;
                continue;
            }
            if (arr[index + 1] % 2 == 0) {
                index += 2;
                continue;
            }
            if (arr[index] % 2 == 0) {
                index += 1;
                continue;
            }
            return true;
        }
        return false;
    }
}


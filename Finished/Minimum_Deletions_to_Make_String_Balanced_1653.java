// 1653. Minimum Deletions to Make String Balanced
import java.util.Arrays;

public class Minimum_Deletions_to_Make_String_Balanced_1653 {
    
}


class Solution {
    public int minimumDeletions(String s) {
        int length = s.length();
        if (length <= 1) {
            return 0;
        }
        if (length == 2 && s.charAt(0) == 'a') {
            return 0;
        } else if (length == 2 && s.charAt(0) == 'b') {
            return 1;
        }
        int[] arr = new int[length];
        int counter = 0;
        for (int i = length - 1; i >= 0; i--) {
            if (s.charAt(i) == 'a') {
                counter++;
            }
            arr[i] = counter;
        }
        // [3,3,2,1,0]
        // [b,a,a,a,b]

        int ans = length;
        int bRemove = 0;
        int i = 0;
        int j = 1;

        while (j < (length - 1)) {
            if (arr[i] == arr[j]) {
                ans = Math.min(ans, bRemove + arr[i]);
                bRemove++;
            }
            i++;
            j++;
        }
        // check last two index if not same
        if (arr[i] != arr[j]) {
            ans = Math.min(ans, bRemove);
        } else {
            ans = Math.min(ans, bRemove + arr[i]);
        }
        return ans;
    }
}

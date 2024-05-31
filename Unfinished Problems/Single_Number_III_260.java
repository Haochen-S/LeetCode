// 260. Single Number III
import java.util.Arrays;

class Solution {
    public int[] singleNumber(int[] nums) {
        if (nums.length == 2) {
            return nums;
        }
        Arrays.sort(nums);

        return nums;
    }
}

public class Single_Number_III_260 {
    
    public static void main(String[] args) {
        int[] arr = {3,4,5,3,4,6};
    
        Solution s = new Solution();
        System.out.println(Arrays.toString(arr));
        System.out.println(Arrays.toString(s.singleNumber(arr)));
    }
}

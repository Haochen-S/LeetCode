
import java.util.Arrays;


// 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

public class Minimum_Difference_Between_Largest_and_Smallest_Value_in_Three_Moves_1509 {
    public static void main(String[] args) {
        int[] nums = new int[] {9,48,92,48,81,31};

        // if (nums.length <= 4) {
        //     return 0;
        // }
        Arrays.sort(nums);
        int firstIndex = 0;
        int lastIndex = nums.length - 1;
        int i = 0;
        while (i < 3) { 
            System.out.println(Arrays.toString(Arrays.copyOfRange(nums, firstIndex, lastIndex + 1)));
            int startGap = nums[firstIndex + 1] - nums[firstIndex];
            int endGap = nums[lastIndex] - nums[lastIndex - 1]; 
            if (startGap >= endGap) {
                firstIndex++;
            } else {
                lastIndex--;
            }
            i++;
        }
        System.out.println(Arrays.toString(Arrays.copyOfRange(nums, firstIndex, lastIndex + 1)));
        // return nums[nums.length-1] - nums[0];
    }
}

class Solution {
    public int minDifference(int[] nums) {
        if (nums.length <= 4) {
            return 0;
        }
        Arrays.sort(nums);
        int ans = nums[nums.length - 1] - nums[0];
        for(int i = 0; i <= 3; i++) {
            ans = Math.min(ans, nums[nums.length - (3 - i) - 1] - nums[i]);
        }
        return ans;
    }
}

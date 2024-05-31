// 260. Single Number III
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] singleNumber(int[] nums) {

        if (nums.length == 2) {
            return nums;
        }
        Arrays.sort(nums);
        ArrayList<Integer> ans = new ArrayList<>();
        int counter = 0;
        
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                i++;
            } else {
                ans.add(nums[i]);
                counter++;
                if (counter == 2) {
                    break;
                }
            }
        }
        if (counter != 2) {
            ans.add(nums[nums.length - 1]);
        }
        int[] intArray = new int[ans.size()];

        for (int i = 0; i < ans.size(); i++) {
            intArray[i] = ans.get(i);
        }
        return intArray;
    }
}

public class Single_Number_III_260 {
    
    public static void main(String[] args) {
        int[] arr = {3,4,5,3,4,6};
    
        Solution s = new Solution();

        System.out.println(Arrays.toString(s.singleNumber(arr)));
    }
}

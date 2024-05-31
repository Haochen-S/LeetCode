// 152. Maximum Product Subarray

public class Maximum_Product_Subarray_152 {
    public static void main(String[] args) {
        int[] arr = {1,-2,-3,-1,1};
    
        SolutionOptimized s = new SolutionOptimized();
        System.out.println(s.maxProduct(arr));
    }
}

class SolutionOptimized {
    public int maxProduct(int[] nums) {
        // Check if the input array is empty, return 0 if it is
        if (nums.length == 0) {
            return 0;
        }

        // Initialize maxSoFar and minSoFar with the first element in the array, and
        // result with maxSoFar
        int maxSoFar = nums[0];
        int minSoFar = nums[0];
        int result = maxSoFar;

        // Loop through the rest of the elements in the array
        for (int i = 1; i < nums.length; i++) {
            int curr = nums[i];

            // Update maxSoFar and minSoFar with the maximum and minimum of curr, maxSoFar *
            // curr, and minSoFar * curr
            // tempMaxSoFar is used to store the value of maxSoFar so that it does not get
            // updated while calculating minSoFar
            int tempMaxSoFar = Math.max(curr, Math.max(maxSoFar * curr, minSoFar * curr));

            minSoFar = Math.min(curr, Math.min(maxSoFar * curr, minSoFar * curr));

            maxSoFar = tempMaxSoFar;

            // Update result with the maximum of maxSoFar and result
            result = Math.max(maxSoFar, result);
        }

        // Return the final result
        return result;
    }
}

class SlowSolution {
    public int maxProduct(int[] nums) {
        int max = nums[0];

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == 0) {
                continue;
            }
            int product = nums[i];
            if (max < product) {
                max = product;
            }
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == 0) {
                    break;
                }
                product *= nums[j];
                if (max < product) {
                    max = product;
                }
            }
        }
        if (nums[nums.length - 1] > max) {
            return nums[nums.length - 1];
        }
        return max;
    }
}


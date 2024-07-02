import java.util.ArrayList;
import java.util.Arrays;

// 350. Intersection of Two Arrays II
public class Intersection_of_Two_Arrays_II_350 {
    public static void main(String[] args) {
        int[] nums1 = new int[] {1,2,3};
        int[] nums2 = new int[] {2,3,4};
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int i = 0;
        int j = 0;
        ArrayList<Integer> result = new ArrayList<Integer>();  
        
        while (i < nums1.length && j < nums2.length) { 
            System.out.println(i);
            System.out.println(j);
            System.out.println("-----");
            if (nums1[i] == nums2[j]) {
                result.add(nums1[i]);
                i++;
                j++;
                continue;
            }
            if (nums1[i] > nums2[j]) {
                j++;
                continue;
            }
            if (nums1[i] < nums2[j]) {
                i++;
            }
        }
        
        int[] ans = new int[result.size()];
 
        // ArrayList to Array Conversion
        for (int counter = 0; counter < result.size(); counter++) {
            ans[counter] = result.get(counter);
            System.out.println(ans[counter]);
        }
    }
}

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int i = 0;
        int j = 0;
        ArrayList<Integer> result = new ArrayList<Integer>();  
        
        while (i < nums1.length && j < nums2.length) { 
            if (nums1[i] == nums2[j]) {
                result.add(nums1[i]);
                i++;
                j++;
                continue;
            }
            if (nums1[i] > nums2[j]) {
                j++;
                continue;
            }
            if (nums1[i] < nums2[j]) {
                i++;
            }
        }
        
        int[] ans = new int[result.size()];
 
        // ArrayList to Array Conversion
        for (int counter = 0; counter < result.size(); counter++)
            ans[counter] = result.get(counter);
        return ans;
    }
}
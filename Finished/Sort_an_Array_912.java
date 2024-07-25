import java.util.Arrays;

public class Sort_an_Array_912 {
    
}

// merge sort in java
class Solution {
    public int[] sortArray(int[] nums) {
        if (nums.length <= 1) {
            return nums;
        }

        int[] arrayA = Arrays.copyOfRange(nums, 0, (int)Math.ceil(nums.length / 2));
        int[] arrayB = Arrays.copyOfRange(nums, (int)Math.ceil(nums.length / 2), nums.length);
        System.out.println(Arrays.toString(arrayA));
        System.out.println(Arrays.toString(arrayB));
        System.out.println("-----");
        arrayA = sortArray(arrayA);
        arrayB = sortArray(arrayB);

        return mergeSort(arrayA, arrayB);
    }

    public int[] mergeSort(int[] arrayA, int[] arrayB) {
        int[] arrayC = new int[arrayA.length + arrayB.length];
        int i = 0;
        int a = 0;
        int b = 0;
        while (arrayA.length > a && arrayB.length > b) {
            if (arrayA[a] > arrayB[b]) {
                arrayC[i] = arrayB[b];
                i++;
                b++;
            } else {
                arrayC[i] = arrayA[a];
                i++;
                a++;
            }
        }
        while (a < arrayA.length) {
            arrayC[i] = arrayA[a];
            i++;
            a++;
        }
        while (b < arrayB.length) {
            arrayC[i] = arrayB[b];
            i++;
            b++;
        }
        System.out.println(Arrays.toString(arrayA));
        System.out.println(Arrays.toString(arrayB));
        System.out.println(Arrays.toString(arrayC));
        return arrayC;
    }
}
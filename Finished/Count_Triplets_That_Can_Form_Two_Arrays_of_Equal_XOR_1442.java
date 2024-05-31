// 1442. Count Triplets That Can Form Two Arrays of Equal XOR

public class Count_Triplets_That_Can_Form_Two_Arrays_of_Equal_XOR_1442 {
  public static void main(String[] args) {
    int[] arr = {1,2,3};

    Solution s = new Solution();
    
    System.out.println(s.countTriplets(arr));
  }
}

class Solution {
  public int countTriplets(int[] arr) {
    int ans = 0;

    for (int i = 0; i < arr.length; i++) {
      for (int j = i + 1; j < arr.length; j++) {

        int a = 0;
        for (int i_ = i; i_ < j; i_++) {
            a ^= arr[i_];
        }

        int b = 0;
        for (int k = j; k < arr.length; k++) {
          b ^= arr[k];
          if (a == b) {
            ans++;
          }
        }
      }
    }
    return ans;
  }
}



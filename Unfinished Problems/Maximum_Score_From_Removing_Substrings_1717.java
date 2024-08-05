// 1717. Maximum Score From Removing Substrings
import java.util.HashMap;
import java.util.ArrayList;

public class Maximum_Score_From_Removing_Substrings_1717 {
    
}

// class Solution {
    

//     public int maximumGain(String s, int x, int y) {
//         // remove "ab" gain x

//         // remove "ba" gain y


//         return 0;
//     }
// }

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        HashMap<int[], Double> map = new HashMap<int[], Double>();
        for (int[] p : points) {
            map.put(p, Math.sqrt(p[0] * p[0] + p[1] * p[1]));
        }
        
        ArrayList<Double> sortedKeys
            = new ArrayList<Double>(map.);
 
        Collections.sort(sortedKeys);
        int i = 0;
        int[][] ans = new int[k][];
        
        // Display the TreeMap which is naturally sorted
        for (Double x : sortedKeys) {
            if (i == k) {
                break;
            }
            ans[i] = map.get(x);
        
            System.out.println("Key = " + x
                               + ", Value = " + map.get(x));
            i++;
        }
        return ans;
    }
}
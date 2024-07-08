public class Water_Bottles_1518 {
    
}

class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int ans = numBottles;
        
        int num = (int)Math.floor(numBottles / numExchange);
        while (num > 0) {
            ans += num;
            numBottles = numBottles - numExchange * num + num;
            num = (int)Math.floor(numBottles / numExchange);
        }

        return ans;
    }
}
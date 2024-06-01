import java.util.Arrays;

public class main {

    public static int minCost(int[] cost, int k) {
        
        int n = cost.length;
        int[] dp = new int[n+1];
        
        // 初始化 dp 数组，所有值设为最大值
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = cost[0];  // 起点的代价

        // 动态规划求解最小代价
        for (int i = 1; i < n; i++) {
            for (int j = Math.max(0, i - k); j < i; j++) {
                dp[i] = Math.min(dp[i], dp[j] + cost[i]);
            }
        }
        
        return dp[n - 1];
    }

    public static void main(String[] args) {
        int[] cost = {11, 9, 2, 6, 1};
        int k = 3;
        System.out.println(minCost(cost, k));  // 输出到达最后一个点的最小代价
    }
}

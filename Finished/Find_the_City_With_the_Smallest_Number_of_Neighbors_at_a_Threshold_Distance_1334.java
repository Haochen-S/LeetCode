import java.util.Arrays;

public class Find_the_City_With_the_Smallest_Number_of_Neighbors_at_a_Threshold_Distance_1334 {
    
}


// Floyd–Warshall algorithm
class Solution {
    // Floyd–Warshall algorithm
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        // Floyd–Warshall algorithm
        double[][] dist = new double[n][n];
        for (double[] row : dist) {
            Arrays.fill(row, Double.POSITIVE_INFINITY);
        }
        for (int i = 0; i < n; i++) {
            dist[i][i] = 0;
        }
        for (int[] edge : edges) {  
            dist[edge[0]][edge[1]] = edge[2];
            dist[edge[1]][edge[0]] = edge[2];
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist[i][j] > dist[i][k] + dist[k][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        // for (double[] row : dist) {
        //     for (double ele : row) {
        //         System.out.print(ele + " ");
        //     }
        //     System.out.println("");
        // }
        int[] citys = new int[n];
        int i = 0;

        for (double[] row : dist) {
            for (double ele : row) {
                if (ele > 0 && ele <= distanceThreshold) {
                    citys[i]++;
                }
            }
            // System.out.println(citys[i]);
            i++;
        }
        int ans = 0;
        int smallest = citys[0];
        i = 0;
        for (int city : citys) {
            if (city <= smallest) {
                ans = i; 
                smallest = city;
            }
            i++;
        }

        return ans;
    }
}



// 1701. Average Waiting Time


public class Average_Waiting_Time_1701 {
    
}


class Solution {
    public double averageWaitingTime(int[][] customers) {
        double totalWaitingTime = 0;
        double preWaitingTimePoint = 0;
        double numOfCustomers = customers.length;
        double timeFinishOrder = 0;

        timeFinishOrder = customers[0][0] + customers[0][1];
        totalWaitingTime += timeFinishOrder - customers[0][0];
        if (numOfCustomers == 1) {
            return totalWaitingTime;
        }

        int i = 1;
        while (i < numOfCustomers) {

            if (timeFinishOrder <= customers[i][0]) {
                timeFinishOrder = customers[i][0] + customers[i][1];
            } else {
                timeFinishOrder = timeFinishOrder + customers[i][1];
            }
            totalWaitingTime += timeFinishOrder - customers[i][0];

            i++;
        }
        return totalWaitingTime / numOfCustomers;
    }
}


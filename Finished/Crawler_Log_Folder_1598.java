public class Crawler_Log_Folder_1598 {
    
}
class Solution {
    public int minOperations(String[] logs) {
        int numOfDepth = 0;
        int i = 0;
        while (i < logs.length) {
            if (logs[i].equals("../")) {
                if (numOfDepth > 0) {
                    numOfDepth--;
                }
            } else if (logs[i].equals("./")) {
                
            } else {
                numOfDepth++;
            }
            i++;
        }
        return numOfDepth;
    }
}
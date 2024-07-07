
// 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

public class Find_the_Minimum_and_Maximum_Number_of_Nodes_Between_Critical_Points_2058 {
    
}

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        int min = -1, max = -1;

        int index = 0;
        int first = -1;
        int last = -1;
        // convert critical points
        ListNode curr = head.next;
        int beforeVal = head.val;
        head.val = 0;
        while (curr.next != null) {
            if (curr.val < beforeVal && curr.val < curr.next.val) {
                beforeVal = curr.val;
                curr.val = 1;
                if (first == -1) {
                    first = index;
                    head = curr;
                } else {
                    last = index;
                }
            } else if (curr.val > beforeVal && curr.val > curr.next.val) {
                beforeVal = curr.val;
                curr.val = 1;
                if (first == -1) {
                    first = index;
                } else {
                    last = index;
                }
            } else {
                beforeVal = curr.val;
                curr.val = 0;
            }
            curr = curr.next;
            index++;
        }
        curr.val = 0;
        if (last == -1 || first == -1) {
            return new int[] {min, max};
        }

        boolean isStart = false;
        int gap = 0;
        while (head.next != null) {
            if (head.val == 0) {
                head = head.next;
                gap++;
                continue;
            }
            if (isStart == false) {
                head = head.next;
                gap = 0;
                isStart = true;
                continue;
            }
            if (min == -1 || min > gap) {
                min = gap;
            }
            gap = 0;
            head = head.next;
        }

         // find min, max
        max = last - first;

        return new int[] {min + 1, max};
    }
}



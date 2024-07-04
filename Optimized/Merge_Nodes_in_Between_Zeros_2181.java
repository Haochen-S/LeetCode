// 2181. Merge Nodes in Between Zeros

public class Merge_Nodes_in_Between_Zeros_2181 {
    
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
    public ListNode mergeNodes(ListNode head) {
        ListNode ans = head;
        ListNode nextNode = head.next;
        int sum = 0;
        while (nextNode.next != null) {
            if (nextNode.val != 0) {
                sum += nextNode.val;
                nextNode = nextNode.next;
            } else {
                head.val = sum;
                head = head.next;
                nextNode = nextNode.next;
                sum = 0;
            }
        }
        head.val = sum;
        head.next = null;
        return ans;
    }
}


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
    public ListNode removeNthFromEnd(ListNode head, int n) {

        //well implemented
        ListNode res = new ListNode(0, head);
        ListNode dummy = res;

        for (int i = 0; i < n; i++) {
            head = head.next;
        }

        while (head != null) {
            head = head.next;
            dummy = dummy.next;
        }

        dummy.next = dummy.next.next;

        return res.next; 
 /* 
        ListNode dummy = head;
        ListNode result = head;
        int dist = 0;

        while(head.next != null){
            if(dist != n) dist++;
            else{
                dummy = dummy.next;
            }
            head = head.next;
        }

        if(dist < n) return result.next;
        if(dummy.next == null) return null;
        dummy.next = dummy.next.next;

        return result; */
    }
}

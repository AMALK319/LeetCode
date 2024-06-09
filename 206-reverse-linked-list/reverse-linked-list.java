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
    public ListNode reverseList(ListNode head) {


        ListNode prev = null, curr = head;
        while(curr != null){
           head = curr;
           curr = head.next;
           head.next = prev;
           prev = head;
        }

        return prev;
        
     




/* 


        !
        ListNode prev = null; 
        while( head != null){
            ListNode next = head.next; 
            head.next = prev; 
            prev = head; 
            head = next; 
        }
        return prev; */
    }

}
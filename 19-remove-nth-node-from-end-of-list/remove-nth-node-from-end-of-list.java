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
 
        ListNode dummy = head;
        int i = 0;
        int m = getNodePosition(head, n);

        if(head.next == null) return null;
        while(dummy.next != null){
            if(i == m-1){
                dummy.next = dummy.next.next;
                return head;
            }
            i++;
            dummy = dummy.next;
        }

        return head.next;

       
    
    }

    private int getNodePosition(ListNode head, int n){
        ArrayList<Integer> temp = new ArrayList<>();
        ListNode dummy = head;

        while(dummy != null){
            temp.add(dummy.val);
            dummy = dummy.next;
        }

        return  temp.size() - n; 
    }
}

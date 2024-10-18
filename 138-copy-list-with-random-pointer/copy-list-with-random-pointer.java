/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/




class Solution {
    public Node copyRandomList(Node head) {

        Node res = new Node(0);
        Node dummyRes = res;
        Map<Node,Node> map = new HashMap<>();
        

        while(head != null){
            if(map.containsKey(head)) dummyRes.next = map.get(head);
            else{
                dummyRes.next = new Node(head.val);
                map.put(head,dummyRes.next);  
            }
            dummyRes = dummyRes.next;
            if(head.random != null && !map.containsKey(head.random)) {
                dummyRes.random = new Node(head.random.val);
                map.put(head.random,dummyRes.random);
            }
            else if (head.random != null) {
                dummyRes.random = map.get(head.random);
            }
            head = head.next;
        }

        return res.next;

    }
}

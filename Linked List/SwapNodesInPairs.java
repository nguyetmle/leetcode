/**
    Given a linked list, swap every two adjacent nodes and return its head. 
    You must solve the problem without modifying the values in the list's nodes 
    (i.e., only nodes themselves may be changed.)
 */

// level: medium
// approach: create 2 pointers prev and cur starting from a dummy node and head, then swap in pairs

class ListNode {
    int val;
    ListNode next;

    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
class SwapNodesInPairs {
    public ListNode swapPairs(ListNode head) {
        if (head==null || head.next==null)
            return head;
        
        ListNode dummy = new ListNode();
        ListNode prev = dummy;
        ListNode cur = head;

        while (cur != null && cur.next != null) {
            //swap the first pair
            prev.next = cur.next;
            cur.next = cur.next.next;
            prev.next.next = cur;

            //move pointers to swap the next pair
            prev = cur;
            cur = cur.next;
        }

        return dummy.next;
    }
}
/**
    Given the head of a linked list, remove the nth node 
    from the end of the list and return its head.
 */

// level: medium
// approach: 2 pointers fast and slow

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class RemoveNthNodeFromEnd {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode slow = head;
        ListNode fast = head;

        //move fast pointer so that the distance between fast and slow pointer is n
        while (n>0) {
            fast = fast.next;
            n--;
        }

        if (fast == null) 
            return head.next;
        
        //move 2 pointers until fast pointer reach the end node
        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }

        //at this point, slow pointer is right before the targeted node
        //remove this node by changing next pointer
        slow.next = slow.next.next;

        return head;
    }
}

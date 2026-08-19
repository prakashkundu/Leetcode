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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode d = new ListNode();
        ListNode c = d;

        while (list1 != null && list2 != null) {

            if (list1.val > list2.val) {
                c.next = list2;
                c = list2;
                list2 = list2.next;
            } else {
                c.next = list1;
                c = list1;
                list1 = list1.next;
            }
        }

        if (list1 != null) {
            c.next = list1;
        } else {
            c.next = list2;
        }

        return d.next;
    }
}
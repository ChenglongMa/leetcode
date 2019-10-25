//You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list. 
//
// You may assume the two numbers do not contain any leading zero, except the number 0 itself. 
//
// Example: 
//
// 
//Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
//Output: 7 -> 0 -> 8
//Explanation: 342 + 465 = 807.
// 
// Related Topics Linked List Math
package leetcode.editor.en;

public class Q2AddTwoNumbers {

    public static void main(String[] args) {
        Solution solution = new Q2AddTwoNumbers().new Solution();
        ListNode l1 = new Q2AddTwoNumbers().new ListNode(5);
//        l1.next = new AddTwoNumbers().new ListNode(4);
//        l1.next.next = new AddTwoNumbers().new ListNode(3);
        ListNode l2 = new Q2AddTwoNumbers().new ListNode(5);
//        l2.next = new AddTwoNumbers().new ListNode(8);
//        l2.next.next = new AddTwoNumbers().new ListNode(4);
        ListNode sum = solution.addTwoNumbers(l1, l2);
        System.out.print(sum.val + " ");
        ListNode n;
        while ((n = sum.next) != null) {
            System.out.print(n.val + " ");
            sum = n;
        }
    }

    public class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }


//leetcode submit region begin(Prohibit modification and deletion)

    /**
     * Definition for singly-linked list.
     * public class ListNode {
     * int val;
     * ListNode next;
     * ListNode(int x) { val = x; }
     * }
     */
    class Solution {

        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            if (l1 == null || l2 == null) {
                return new ListNode(0);
            }

            int quo = 0;
            ListNode res = new ListNode(0), curr = res;
            do {
                if (l1 == null) {
                    l1 = new ListNode(0);
                }
                if (l2 == null) {
                    l2 = new ListNode(0);
                }
                int v1 = l1.val, v2 = l2.val;
                int sum = (v1 + v2) + quo;
                int q = sum / 10;
                int rem = sum - 10 * q;
                curr.next = new ListNode(rem);
                quo = q;
                curr = curr.next;
                l1 = l1.next;
                l2 = l2.next;
            } while (l1 != null || l2 != null || quo != 0);
            return res.next;
        }

    }

//leetcode submit region end(Prohibit modification and deletion)

}
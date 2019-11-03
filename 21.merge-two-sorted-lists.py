#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (49.66%)
# Likes:    2826
# Dislikes: 412
# Total Accepted:    730K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#
#


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        (smaller, bigger) = (l1, l2)

        res = ListNode(0)
        curr = res
        while smaller is not None:
            if bigger is not None and smaller.val > bigger.val:
                (smaller, bigger) = (bigger, smaller)
            curr.next = smaller
            curr = curr.next
            smaller = smaller.next

        while bigger is not None:
            curr.next = bigger
            curr = curr.next
            bigger = bigger.next

        return res.next


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next = ListNode(4)
    # res = s.mergeTwoLists(l1, l2)
    res = l2
    while res is not None:
        print(res.val)
        res = res.next

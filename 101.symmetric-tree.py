#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (44.80%)
# Likes:    2844
# Dislikes: 65
# Total Accepted:    493.6K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
#
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#
#


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def isSymmetric(left: TreeNode, right: TreeNode) ->bool:
    if not left:
        return not right
    if not right:
        return False

    return left.val == right.val and isSymmetric(left.left, right.right) and isSymmetric(left.right, right.left)


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left:
            return not root.right
        if not root.right:
            return not root.left
        if root.left.val != root.right.val:
            return False
        return isSymmetric(root.left, root.right)


# @lc code=end

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)
    s = Solution()
    left = root.left
    right = root.right
    print(s.isSymmetric(root))

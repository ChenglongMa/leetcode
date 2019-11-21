#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (29.78%)
# Likes:    875
# Dislikes: 180
# Total Accepted:    191.2K
# Total Submissions: 640.6K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
#
# For example:
#
#
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB
# ⁠   ...
#
#
# Example 1:
#
#
# Input: 1
# Output: "A"
#
#
# Example 2:
#
#
# Input: 28
# Output: "AB"
#
#
# Example 3:
#
#
# Input: 701
# Output: "ZY"
#
#

# @lc code=start


class Solution:

    def convertToTitle(self, n: int) -> str:
        res = ""
        while n > 0:
            res = chr(65 + (n - 1) % 26) + res
            n = (n - 1) // 26
        return res

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(123456))

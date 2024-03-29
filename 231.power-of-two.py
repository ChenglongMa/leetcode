#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (42.48%)
# Likes:    557
# Dislikes: 148
# Total Accepted:    259.8K
# Total Submissions: 610K
# Testcase Example:  '1'
#
# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
#
# Input: 1
# Output: true
# Explanation: 2^0 = 1
#
#
# Example 2:
#
#
# Input: 16
# Output: true
# Explanation: 2^4 = 16
#
# Example 3:
#
#
# Input: 218
# Output: false
#
#

# @lc code=start


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(32):
            if n == 1 << i:
                return True
        return False

# @lc code=end

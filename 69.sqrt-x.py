#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (32.35%)
# Likes:    945
# Dislikes: 1580
# Total Accepted:    439.4K
# Total Submissions: 1.4M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
#
# Example 1:
#
#
# Input: 4
# Output: 2
#
#
# Example 2:
#
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
# the decimal part is truncated, 2 is returned.
#
#
#

# @lc code=start


class Solution:

    def mySqrt(self, x: int) -> int:
        """
        Newton's method
        """
        res = x
        while res ** 2 > x:
            res = (res + x // res) // 2
        return res

    def mySqrt2(self, x: int) -> int:
        """
        Binary search
        """
        if x <= 1:
            return x
        left = 0
        right = x
        while left < right:
            mid = (left+right)//2
            if x // mid >= mid:
                left = mid + 1
            else:
                right = mid

        return right - 1

# @lc code=end

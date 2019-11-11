#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.74%)
# Likes:    1057
# Dislikes: 1834
# Total Accepted:    467.5K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
#
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
#
from typing import List
# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        sum = digits[-1]+1
        if sum < 10:
            digits[-1] = sum
            return digits
        d = 1
        sum -= 10
        digits[-1] = sum
        for i in range(2, len(digits)+1):
            sum = digits[-i]+d
            digits[-i] = sum % 10
            d = sum//10
            if not d:
                break

        return digits if not d else [d]+digits

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([9, 9]))

#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (31.92%)
# Likes:    1805
# Dislikes: 686
# Total Accepted:    370.4K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
#
# Example 1:
#
#
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#
# Example 2:
#
#
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
# Note:
#
#
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
#
#
from typing import List
# @lc code=start


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        count = 0
        for i in range(length):
            prev = nums[i]
            nxt = (i + k) % length
            while nxt != i:
                tmp = nums[nxt]
                nums[nxt] = prev
                prev = tmp
                nxt = (nxt + k) % length
                count += 1
            nums[nxt] = prev
            count += 1
            if count == length:
                return


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    nums = list(range(4))
    s.rotate(nums,2)
    print(nums)

#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (41.25%)
# Likes:    1615
# Dislikes: 207
# Total Accepted:    476.7K
# Total Submissions: 1.2M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
#
# Input: [1,3,5,6], 5
# Output: 2
#
#
# Example 2:
#
#
# Input: [1,3,5,6], 2
# Output: 1
#
#
# Example 3:
#
#
# Input: [1,3,5,6], 7
# Output: 4
#
#
# Example 4:
#
#
# Input: [1,3,5,6], 0
# Output: 0
#
#
#
from typing import List
# @lc code=start


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target == nums[-1]:
            return len(nums) - 1
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] < target:
                i = mid+1
            if nums[mid] > target:
                j = mid-1
            if nums[mid] == target:
                return mid
        return i


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 4, 5, 6], 3))

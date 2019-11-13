#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (37.26%)
# Likes:    1408
# Dislikes: 3237
# Total Accepted:    445.4K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
#
# Note:
#
#
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
#
#
# Example:
#
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#
#
from typing import List
# @lc code=start


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m + n - 1
        while index >= 0:
            if n < 1 or m > 0 and nums1[m-1] >= nums2[n-1]:
                nums1[index] = nums1[m-1]
                m -= 1
            elif m < 1 or n > 0 and nums1[m-1] <= nums2[n-1]:
                nums1[index] = nums2[n-1]
                n -= 1
            index -= 1

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    nums = [2, 0]
    s.merge(nums, 1, [1], 1)
    print(nums)

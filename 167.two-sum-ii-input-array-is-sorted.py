#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (51.70%)
# Likes:    1164
# Dislikes: 471
# Total Accepted:    311.9K
# Total Submissions: 601.6K
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2.
#
# Note:
#
#
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
#
#
# Example:
#
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
#
#

# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = -1
        length = len(numbers)
        while True:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, length + j + 1]
            if sum < target:
                i += 1
            else:
                j -= 1

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            if numbers[i] in dic:
                return [dic[numbers[i]], i + 1]
            dic[target - numbers[i]] = i + 1


# @lc code=end

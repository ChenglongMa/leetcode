#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = target
        nums.sort()
        min_diff = 99999
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff = abs(s - target)
                if diff < min_diff:
                    min_diff = diff
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
        return res


# @lc code=end

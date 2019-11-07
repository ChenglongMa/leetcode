#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.30%)
# Likes:    1706
# Dislikes: 1534
# Total Accepted:    576.1K
# Total Submissions: 1.7M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
from typing import List

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not len(strs):
            return ''
        if len(strs)==1:
            return strs[0]
        temp = []
        for c in strs[0]:
            temp.append(c)

        for s in range(1,len(strs)):
            item = strs[s]
            i = 0
            if len(temp)>len(item):
                temp[len(item)]=None
            for i in range(min(len(temp),len(item))):
                if not temp[i]:
                    break
                if temp[i] != item[i]:
                    temp[i] = None
                    break

        res=''
        for t in temp:
            if not t:
                break
            res+=t
        return res

# @lc code=end

if __name__ == "__main__":
    i = 0
    for i in range(1):
        pass
    print(i)
    s=Solution()
    print(s.longestCommonPrefix(["abab","aba",'a']))
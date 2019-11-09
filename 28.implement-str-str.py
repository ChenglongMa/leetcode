#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (33.16%)
# Likes:    1116
# Dislikes: 1549
# Total Accepted:    521.2K
# Total Submissions: 1.6M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Example 1:
#
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or needle == '':
            return 0
        len_diff = len(haystack)-len(needle)
        if len_diff <= 0:
            return 0 if haystack == needle else -1
        i = 0
        j = 0
        index = -1
        next_start = 0
        temp = []
        while j < len(haystack) and i < len(needle):
            if i and haystack[j] == needle[0]:
                temp.append(j)
            if haystack[j] == needle[i]:
                index = j if index == -1 else index
                next_start = index
                i += 1
                j += 1
            else:
                index = -1
                next_start += 1
                i = 0
                j = temp.pop(0) if temp else next_start
        return index if index <= len_diff else -1
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.strStr('mississippi', 'issipi'))
    a = [1, 2, 3, 4]
    print(a.pop(0))

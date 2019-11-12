#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (41.12%)
# Likes:    1231
# Dislikes: 229
# Total Accepted:    357.5K
# Total Submissions: 867.4K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#

# @lc code=start


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))+1
        d = 0
        res = ''
        for i in range(1, length):
            x = int(a[-i]) if i <= len(a) else 0
            y = int(b[-i]) if i <= len(b) else 0
            sum = x + y + d
            d = sum//2
            res = f'{sum%2}{res}'

        return f'1{res}' if d else res


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.addBinary('1111', '1111'))

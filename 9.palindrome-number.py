#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (45.44%)
# Likes:    1698
# Dislikes: 1410
# Total Accepted:    717.4K
# Total Submissions: 1.6M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
#
# Example 1:
#
#
# Input: 121
# Output: true
#
#
# Example 2:
#
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Follow up:
#
# Coud you solve it without converting the integer to a string?
#
#

# @lc code=start


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        res = 0
        while x > res:
            res = res*10+x % 10
            x //= 10
        return res == x or x == res//10

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(10))
    print(s.isPalindrome(121))
    print(s.isPalindrome(123321))
    print(s.isPalindrome(0))

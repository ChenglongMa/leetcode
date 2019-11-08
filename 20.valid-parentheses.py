#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.48%)
# Likes:    3577
# Dislikes: 174
# Total Accepted:    746.9K
# Total Submissions: 2M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#
#

# @lc code=start


class Solution:
    syms = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    def isValid(self, s: str) -> bool:
        if not s or not len(s):
            return True
        curr = []
        for c in s:
            if c in self.syms:
                curr.append(c)
            elif not curr or not self.syms[curr.pop()] == c:
                return False
        return not curr

# @lc code=end


if __name__ == "__main__":
    l = []
    if l:
        print('not empty')
    if not l:
        print('empty')

#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (42.12%)
# Likes:    939
# Dislikes: 7514
# Total Accepted:    328.6K
# Total Submissions: 779.3K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
#
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a
# string.
#
#
#
# Example 1:
#
#
# Input: 1
# Output: "1"
#
#
# Example 2:
#
#
# Input: 4
# Output: "1211"
#
#

# @lc code=start


def describe_int(n: str)->str:
    if not n:
        return ''
    curr = n[0]
    n_count = 1
    des = ''
    for i in range(1, len(n)):
        c = n[i]
        if curr == c:
            n_count += 1
        else:
            des += f'{n_count}{curr}'
            curr = c
            n_count = 1
    return des+f'{n_count}{curr}'


class Solution:
    elements = ['1']

    def countAndSay(self, n: int) -> str:
        length = len(self.elements)
        if n <= length:
            return self.elements[n-1]
        for i in range(n - length):
            self.elements.append(describe_int(self.elements[-1]))
        return self.elements[-1]

# @lc code=end


if __name__ == "__main__":
    print(describe_int('1'))

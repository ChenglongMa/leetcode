#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (30.07%)
# Likes:    1386
# Dislikes: 468
# Total Accepted:    285.2K
# Total Submissions: 945.3K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
#

# @lc code=start


class Solution:
    def isPrime(self, n: int)->bool:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        primes = []
        is_prime = [0,0] + [1]*(n-2)
        
        for num in range(2,n):
            if is_prime[num]:
                primes.append(num)
                for j in range(num, n, num):
                    is_prime[j] = 0
        return len(primes)

# @lc code=end

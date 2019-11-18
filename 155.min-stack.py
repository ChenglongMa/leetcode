#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (39.43%)
# Likes:    2284
# Dislikes: 245
# Total Accepted:    372.3K
# Total Submissions: 939K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
#
#
#
# Example:
#
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
#
#
#
#
#

# @lc code=start

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []  # (val,min)

    def push(self, x: int) -> None:
        min_val = x if x < self.getMin() else self.getMin()
        self.stack.append((x, min_val))

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else float('inf')


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

if __name__ == "__main__":
    s = MinStack()
    s.push(0)
    s.push(1)
    s.push(0)
    s.getMin()
    s.pop()
    s.pop()
    s.top()
    print(s.getMin())

# 155. Min Stack

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

class MinStack:
    # Brute force solution with O(n) time complexity for getMin()
    # def __init__(self):
    #     self.stack = []

    # def push(self, val: int):
    #     self.stack.append(val)

    # def pop(self) -> None:
    #     self.stack.pop() 

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return min(self.stack)
    def __init__(self):
        self.stack = []
        self.minValStack = []

    def push(self, val: int):
        self.stack.append(val)

        if len(self.minValStack) == 0:
            self.minValStack.append(val)
        else:
            self.minValStack.append(min(val, self.minValStack[-1]))    

    def pop(self) -> None:
        self.stack.pop()
        self.minValStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # O(n)
        # return min(self.stack)
        return self.minValStack[-1]
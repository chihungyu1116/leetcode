# http://oj.leetcode.com/problems/jump-game-ii/
# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# For example:
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)



# Recursion solution (Very Slow):

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        return self.sol(A, 0, 0)
        
    def sol(self, A, index, count):
        if index >= (len(A) - 1):
            return count
            
        steps = A[index]
        if steps == 0:
            return float("inf")
            
        r = []
        for i in range(1, steps + 1):
            r.append(self.sol(A, index + i, count + 1))
        
        return min(r)

# Solution 2 ( O(n) solution )

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        lenA = len(A)
        if lenA == 1:
            return 0
        i = currentMax = jumps = 0
        
        while i < lenA:
            currentMax = A[i] + i
            if A[i] > 0:
                jumps += 1
            else:
                return 0
            
            if currentMax >= lenA - 1:
                return jumps
            
            tempMax = 0
            for j in range(i+1, currentMax + 1):
                if A[j] + j >= tempMax:
                    tempMax = A[j] + j
                    i = j
                    
        return jumps
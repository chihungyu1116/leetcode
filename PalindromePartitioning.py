# http://oj.leetcode.com/problems/palindrome-partitioning/
# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return

#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]

# Solved via Dynamic Programming
# First create (N + 1) x (N + 1) matrix, N is the length of s, and s is the sentence
# Traverse through the matrix, let f(i, j) represent the substring of s -> s[i:j]
# Then we end up with matrix like this for s = "aab"
# 0 0 0 0
# 1 0 0 0
# 1 1 0 0
# 0 0 1 0

# Then start from the last row, if the col on the last row, has value == 1 then we use the col index as row
#   and check that row if it contains value of col == 1
#   perform the above procedure recursively till the row index == 0
#   for each procedure performed above, append the substring s[col:row] to the index if value of col == 1
#   return the result and problem solved!

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        matrix = self.getMatrix(s)
        matrix = self.setPalindromeOnMatrix(s, matrix)
        
        result = []
        lastRowIndex = len(matrix) - 1
        self.getSols(s, matrix, lastRowIndex, [], result)
        
        return result
        
    def getSols(self, s, matrix, rowIndex, currentResult, finalResult):
        if rowIndex == 0:
            finalResult.append(currentResult)
            return
            
        row = matrix[rowIndex]
        for colCurrentIndex, colCurrentVal in enumerate(row):
            if colCurrentVal == 1:
                str = s[colCurrentIndex:rowIndex]
                tempResult = currentResult[:]
                tempResult.insert(0, str)
                self.getSols(s, matrix, colCurrentIndex, tempResult, finalResult)
        
    def isPalindrome(self, s):
        if len(s) == 1:
            return True
            
        head = 0
        tail = len(s) - 1
        
        while head < tail:
            if s[head] != s[tail]:
                return False
            head+=1
            tail-=1
        return True
        
    def getMatrix(self, s):
        sLen = len(s) + 1
        result = []
        for i in range(sLen):
            row = []
            for j in range(sLen):
                row.append(0)
            result.append(row)
        return result
        
    def setPalindromeOnMatrix(self, s, matrix):
        mLen = len(matrix)
        mRange = range(mLen)
        for row in mRange:
            for col in mRange:
                if row > col:
                    str = s[col:row]
                    if self.isPalindrome(str):
                        matrix[row][col] = 1
        return matrix
        
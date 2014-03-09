# http://oj.leetcode.com/problems/3sum/
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
# The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},

#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3:
            return []
        
        num.sort()
        result = []
        i = 0
                    
        if len(num) < 3:
            return result
    
        while i < len(num):
            j = i + 1
            k = len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == 0:
                    triplet = [num[i], num[j], num[k]]
                    if self.notContain(result, triplet):
                        result.append(triplet)
                    j+=1
                elif sum > 0:
                    k-=1
                else:
                    j+=1
                
            i+=1
        return result
        
    def notContain(self, result, triplet):
        for r in result:
            if r == triplet:
                return False
        return True
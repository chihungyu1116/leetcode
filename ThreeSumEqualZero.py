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
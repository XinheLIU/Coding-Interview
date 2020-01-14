class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        # write your code here
        can_still_flip, no_more_flips, max_ones = 0, 0, 0
        
        for num in nums:
            
            if num == 1:
                can_still_flip += 1 
                no_more_flips += 1
            else:
                can_still_flip += 1 
                no_more_flips, can_still_flip = can_still_flip, 0
                
            max_ones = max(max_ones, can_still_flip, no_more_flips)

        return max_ones
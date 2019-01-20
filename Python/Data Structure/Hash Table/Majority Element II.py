class Solution:
	# Moore Voting
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1,count1 = None,0
        num2,count2 = None,0
        for x in nums:
            if x == num1:
                count1 += 1
            elif x == num2:
                count2 += 1
            elif count1 == 0:
                num1,count1 = x,1
            elif count2 == 0:
                num2,count2 = x,1
            else:
                count1 -= 1
                count2 -= 1

        count1,count2 = 0,0
        for x in nums:# 统计确定候选值是真的主要元素
            if x == num1:
                count1 += 1
            if x == num2:
                count2 += 1
        res = []
        if count1 > len(nums)//3:
            res.append(num1)
        if count2 > len(nums)//3:
            res.append(num2)
        return res
        
    '''
    # hash map
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for x in nums:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
        for key,value in dic.items():
            if value > len(nums) / 3:
                ret.append(key)
        return ret
    '''
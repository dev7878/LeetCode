class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        output = 0
        for i in range(len(nums)):
            output ^=  nums[i]

        return output

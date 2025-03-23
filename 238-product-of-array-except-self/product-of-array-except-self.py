class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # [1,2,3,4]
        # pre - [1,1,2,6]
        # post - [24,12,4,1]

        result = [1]*len(nums)

        prefix = 1 
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1,-1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


        
        
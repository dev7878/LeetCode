class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        i=0
        if nums[0] == 1:
            return 0
        while i < len(nums) -1:
            if nums[i] != (nums[i+1] - 1): 
                return nums[i]+1
            else: 
                i+=1
        if (i+1) == len(nums):
            return len(nums)
        
        

    
       
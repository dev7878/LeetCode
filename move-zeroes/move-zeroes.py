class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        snowball_size = 0 

        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[snowball_size], nums[i] = nums[i], nums[snowball_size]
                snowball_size+=1

    
        return nums

            
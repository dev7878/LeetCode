class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr_hash = {}
        
        for i in range(len(nums)):
            checker = (target - nums[i]) 
            if checker in arr_hash:
                return [i,arr_hash[checker] ]
            arr_hash[nums[i]] = i
        return []
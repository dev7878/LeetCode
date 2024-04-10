class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        number_hash = {} 

        # itration 
        for index, num in enumerate(nums):
            # saving complement for tracking backing in dictonary 
            complement = target - num 

            if complement in number_hash:
                return [number_hash[complement], index]

            number_hash[num] = index 

        return []

        
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_set = set(nums)
        max_length = 0 

        for num in nums_set:

            if num-1 not in nums_set:
                streak = 1 
                current = num 

                while current+1 in nums_set:
                    streak +=1 
                    current +=1 

                max_length = max(max_length, streak)

        return max_length
        
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        # Iterate over the array
        for index, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            # If the complement exists in our dictionary, we have found a pair
            if complement in num_to_index:
                return [num_to_index[complement], index]
            # Add the current number to the dictionary
            num_to_index[num] = index
        # If no pair is found, return an empty list (or an error)
        return []
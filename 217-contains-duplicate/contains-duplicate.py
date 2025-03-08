class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashs = set()
        for num in nums:
            if num in hashs:
                return True 
            hashs.add(num)
        return False
        
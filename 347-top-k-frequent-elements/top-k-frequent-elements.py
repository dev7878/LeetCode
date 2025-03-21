from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
            # Step 1: Build the frequency map
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # Step 2: Bucket the numbers by frequency
        # The index represents frequency, and the value at that index is a list of numbers
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Step 3: Gather the top k frequent elements
        result = []
        for freq in range(len(buckets) - 1, 0, -1):  # Start from highest frequency
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        
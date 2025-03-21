class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq_map = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1+ count.get(n,0)
        for num, freq in count.items():
            freq_map[freq].append(num)

        # print(freq_map) 

        result = []

        for i in range(len(freq_map)-1, 0 , -1):
            
            for n in freq_map[i]:
                result.append(n)
                if len(result) == k:
                    return result
        

        
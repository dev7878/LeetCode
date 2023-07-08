class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        temp_max = max(candies)
        output = []

        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= temp_max:
                output.append(True)
            else:
                output.append(False)
        
        return output
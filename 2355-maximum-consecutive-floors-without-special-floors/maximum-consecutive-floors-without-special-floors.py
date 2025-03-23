class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """

        # looking for gaps
        # sort special arr  
        # check gap between bottom and special[0]
        # check gaps between two specials 
        # check gap between special[-1] and top 
        # return highest

        
        floor_gap_arr = [bottom-1] + sorted(special) + [top+1]

        res = 0
        for i in range(1, len(floor_gap_arr)):
            res = max(res, floor_gap_arr[i]-floor_gap_arr[i-1]-1)
        return res
            



        
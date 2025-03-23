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

        special.sort()

        inter_gap = 0 

        bottom_gap = special[0] - bottom 

        for i in range(1,len(special)):

            gap = special[i] - special[i-1] -1 
            inter_gap = max(gap, inter_gap) 

        top_gap = top - special[-1] 

        return max(bottom_gap,inter_gap,top_gap )

            



        
class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        # [ [0,n-1], [n,2*n-1], [2*n, 3*n-1]]
        
        output = []
        if m*n != len(original):
            return output
        else:
            itr = 0 
            for i in range(m):
                m_row = []
                for j in range(n):
                    m_row.append(original[itr])
                    itr+=1
                output.append(m_row)
        return output

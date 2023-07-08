class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ""
        
        total_length = len(word1)+len(word2)

        for i in range(total_length):
            
            if i < len(word1):
                output += word1[i]
            if i<len(word2):
                output+=word2[i]

        return output

        
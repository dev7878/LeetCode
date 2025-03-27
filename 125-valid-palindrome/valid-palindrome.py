class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()

        left = 0 
        right = len(s)-1
        res = True

        while left < right:
            
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right -=1
            else:

                if s[left] != s[right]:
                    res = False
                    return res
                else:
                    left +=1
                    right -=1 


        return res
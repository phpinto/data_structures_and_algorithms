class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        min_l = len(s)
        max_r = -1
        
        for i in range(len(s)):
            l, r = i, i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > (max_r - min_l):
                    min_l, max_r = l, r
                l -= 1
                r += 1
            
            l, r = i, i + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > (max_r - min_l):
                    min_l, max_r = l, r
                l -= 1
                r += 1  
                
        return s[min_l:(max_r + 1)]
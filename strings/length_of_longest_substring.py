class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        lp, rp = 0, 1
        char_set = {s[lp]}
        longest = 1
       
        while rp < len(s):
            if s[rp] not in char_set:
                p_diff = rp - lp + 1
                if p_diff > longest:
                    longest = p_diff
                char_set.add(s[rp])
            else:
                while s[lp] != s[rp]:
                    char_set.remove(s[lp])
                    lp += 1 
                lp += 1        
            rp += 1
                
        return longest
            